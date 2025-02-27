def find_primes_between_indices(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    start_index, end_index = (30, 43)
    primes = [num for num in lst[start_index:end_index + 1] if is_prime(num)]
    return sorted(primes)