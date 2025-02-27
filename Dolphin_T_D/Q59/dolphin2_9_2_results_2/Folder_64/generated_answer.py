def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(x):
    if isinstance(x, tuple) and len(x) > 4:
        x = x[4]
    prime_nums = []
    for i in range(2, x):
        if is_prime(i):
            num = i
            while num != 0:
                if not is_prime(num):
                    break
                num //= 10
            else:
                prime_nums.append(i)
    return sorted(prime_nums)