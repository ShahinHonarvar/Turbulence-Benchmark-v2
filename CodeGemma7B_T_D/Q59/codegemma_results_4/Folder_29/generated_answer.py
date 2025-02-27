def all_left_truncatable_prime(tup):
    primes = []
    for num in range(tup[55]):
        if str(num) not in '0' and all((prime_test(int(num[i:])) for i in range(1, len(str(num))))):
            primes.append(num)
    return sorted(primes, reverse=True)

def prime_test(n):
    if n in [0, 1, 4, 6, 8, 9]:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True