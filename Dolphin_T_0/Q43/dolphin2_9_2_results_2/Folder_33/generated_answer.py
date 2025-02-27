def find_primes_between_indices(lst):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    prime_list = [num for num in lst[289:382] if is_prime(num)]
    return sorted(prime_list, reverse=True) if prime_list else []