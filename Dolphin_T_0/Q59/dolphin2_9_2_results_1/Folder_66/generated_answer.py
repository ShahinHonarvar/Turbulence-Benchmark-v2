def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(t):
    x = t[25]
    prime_nums = []
    for num in range(x - 1, 1, -1):
        if is_prime(num):
            decrement_num = num
            while decrement_num > 0:
                if not is_prime(decrement_num):
                    break
                decrement_num //= 10
                if decrement_num == 0:
                    prime_nums.append(num)
    prime_nums.sort(reverse=True)
    return prime_nums