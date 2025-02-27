def find_primes_between_indices(lst):

    def is_prime(number):
        if number <= 1:
            return False
        if number <= 3:
            return True
        if number % 2 == 0 or number % 3 == 0:
            return False
        i = 5
        while i * i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                return False
            i += 6
        return True
    primes = [num for num in lst[3:9] if is_prime(num)]
    return sorted(primes)