def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def prime_factors(lst):
    num = lst[702]
    factors = set()
    i = 2
    while i * i <= num:
        if num % i == 0:
            if is_prime(i):
                factors.add(i)
            num = num / i
        else:
            i += 1
    if num > 1:
        if is_prime(int(num)):
            factors.add(int(num))
    return factors