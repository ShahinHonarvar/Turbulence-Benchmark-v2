def find_primes_between_indices(num_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    prime_list = [i for i in num_list[14:69] if is_prime(i)]
    return sorted(prime_list, reverse=True) if prime_list else []