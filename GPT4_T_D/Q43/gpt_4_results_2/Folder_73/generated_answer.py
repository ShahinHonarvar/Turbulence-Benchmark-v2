def find_primes_between_indices(lst):

    def check_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = [i for i in lst[19:91] if check_prime(i)]
    primes.sort(reverse=True)
    return primes