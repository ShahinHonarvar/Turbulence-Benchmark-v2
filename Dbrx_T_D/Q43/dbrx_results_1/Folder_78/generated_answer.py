def find_primes_between_indices(input_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    prime_numbers = [num for num in input_list[28:83] if is_prime(num)]
    return sorted(prime_numbers)