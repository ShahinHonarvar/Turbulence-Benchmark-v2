def find_primes_between_indices(one_arg):

    def is_prime(n):
        if n == 2:
            return True
        if n % 2 == 0 or n == 1:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    primes = [num for num in one_arg[45:81] if is_prime(num)]
    return sorted(primes, reverse=True)