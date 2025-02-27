def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(args):
    x = args[992]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            n = num
            while n != 0:
                if not is_prime(n):
                    break
                n //= 10
            else:
                primes.append(num)
    return sorted(primes)