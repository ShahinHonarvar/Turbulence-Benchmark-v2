def find_primes_between_indices(nums_list):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    return sorted([num for num in nums_list[3:9] if is_prime(num)])