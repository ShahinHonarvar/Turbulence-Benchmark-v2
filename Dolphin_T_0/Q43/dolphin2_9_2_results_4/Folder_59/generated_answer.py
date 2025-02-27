def find_primes_between_indices(lst):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    return sorted([num for num in lst[4:9] if is_prime(num)], reverse=True)