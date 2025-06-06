def find_primes_between_indices(int_list):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = [num for idx, num in enumerate(int_list) if 23 <= idx <= 75 and is_prime(num)]
    return sorted(primes, reverse=True)