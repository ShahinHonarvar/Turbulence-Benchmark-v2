def all_left_right_truncatable_prime(t):
    x = t[93]
    prime_list = []
    for num in range(2, x + 1):
        if zero_in_num(num) or not is_prime(num):
            continue
        temp = num
        while True:
            if temp < 10:
                prime_list.append(num)
                break
            if not is_prime(temp):
                break
            temp //= 10
            temp %= 10
    return sorted(prime_list)

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqr = int(n ** 0.5) + 1
    for div in range(3, sqr, 2):
        if n % div == 0:
            return False
    return True

def zero_in_num(n):
    while n > 0:
        if n % 10 == 0:
            return True
        n //= 10
    return False