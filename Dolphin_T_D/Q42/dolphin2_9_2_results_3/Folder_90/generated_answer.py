def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def prime_factors(lst):
    num = lst[263]
    set_prime_factors = set()
    i = 2
    while i * i <= num:
        if num % i == 0:
            if is_prime(i):
                set_prime_factors.add(i)
            if i != num // i:
                if is_prime(num // i):
                    set_prime_factors.add(num // i)
        i += 1
    return set_prime_factors