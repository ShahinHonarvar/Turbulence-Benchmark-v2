def find_primes_between_indices(autre_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    return sorted([autre_list[i] for i in range(229, 851) if is_prime(autre_list[i])], reverse=True)