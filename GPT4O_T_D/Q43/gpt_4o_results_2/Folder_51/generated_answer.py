def find_primes_between_indices(numbers):

    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True
    if len(numbers) < 15:
        return []
    primes = [num for num in numbers[14:69] if is_prime(num)]
    return sorted(primes, reverse=True)