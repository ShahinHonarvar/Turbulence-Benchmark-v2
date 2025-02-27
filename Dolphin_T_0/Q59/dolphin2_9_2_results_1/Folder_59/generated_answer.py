def all_left_truncatable_prime(numbers):

    def check_left_truncatable(number):
        while number:
            if not is_prime(number):
                return False
            number = number // 10
        return True
    x = numbers[84]
    primes = [number for number in range(2, x) if is_prime(number)]
    primes = list(filter(lambda prime: check_left_truncatable(prime), primes))
    primes.sort(reverse=True)
    return primes