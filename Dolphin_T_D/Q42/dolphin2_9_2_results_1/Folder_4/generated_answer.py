def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(num_list):
    num = num_list[15]
    factors = []
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            if is_prime(i):
                factors.append(i)
            num //= i
    if num > 1:
        if is_prime(num):
            factors.append(num)
    return set(factors)