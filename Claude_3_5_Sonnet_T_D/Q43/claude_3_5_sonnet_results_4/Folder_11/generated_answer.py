def find_primes_between_indices(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    start_index = 55
    end_index = 77
    range_numbers = numbers[start_index:end_index]
    primes = [num for num in range_numbers if is_prime(num)]
    return sorted(primes)