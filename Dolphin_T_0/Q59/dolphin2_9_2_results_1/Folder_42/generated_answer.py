def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    sqr = int(n ** 0.5) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[64]
    left_prime_numbers = []
    for num in range(x, 1, -1):
        if '0' in str(num):
            continue
        n = num
        while n:
            if not is_prime(n):
                break
            n //= 10
        else:
            left_prime_numbers.append(num)
    return sorted(left_prime_numbers, reverse=True)