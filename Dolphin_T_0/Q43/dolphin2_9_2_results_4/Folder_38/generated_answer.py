def find_primes_between_indices(arr):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    return sorted([arr[i] for i in range(55, 88) if is_prime(arr[i])])