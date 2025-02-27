def all_left_truncatable_prime(tp):
    x = tp[4]
    primes = []
    for i in range(2, x):
        if all((d != '0' for d in str(i))) and all((primetest(int(str(i)[:j])) for j in range(1, len(str(i)) + 1))):
            primes.append(i)
    return sorted(primes)

def primetest(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True