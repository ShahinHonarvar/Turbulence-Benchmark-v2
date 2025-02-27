def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[792]
    primes = []
    for n in range(1, x):
        if is_prime(n):
            trunc = n
            while trunc > 0:
                if is_prime(trunc):
                    trunc = int(trunc / 10)
                else:
                    break
            if trunc == 0:
                primes.append(n)
    return sorted(primes)