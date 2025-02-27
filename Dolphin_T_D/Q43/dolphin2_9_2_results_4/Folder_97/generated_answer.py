def find_primes_between_indices(numbers):

    def is_prime(n):
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i:
                i += 2
            else:
                return False
        return True
    primes = [num for num in numbers[295:456] if is_prime(num)]
    return sorted(primes, reverse=True)