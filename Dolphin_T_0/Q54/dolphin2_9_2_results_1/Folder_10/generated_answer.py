def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(args):
    x = args[38]
    primes = []
    for num in range(x, 0, -1):
        trunc = num
        while trunc > 0 and is_prime(trunc):
            primes.append(trunc)
            trunc //= 10
    return sorted(list(set(primes)), reverse=True)