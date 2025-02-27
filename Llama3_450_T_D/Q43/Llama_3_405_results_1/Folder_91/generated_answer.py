def find_primes_between_indices(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    try:
        start = numbers[0]
        end = numbers[1]
    except IndexError:
        return []
    prime_numbers = [i for i in range(start, end + 1) if is_prime(i)]
    return sorted(prime_numbers)