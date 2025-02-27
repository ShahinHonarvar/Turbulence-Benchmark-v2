def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(x):

    def is_left_truncatable(n):
        s = str(n)
        for i in range(len(s) - 1, 0, -1):
            if not is_prime(int(s[i:])):
                return False
        return True
    primes = []
    for i in range(remove_zeros(x) + 1):
        if is_prime(i) and is_left_truncatable(i):
            primes.append(i)
    return primes