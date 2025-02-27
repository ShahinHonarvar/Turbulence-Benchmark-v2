def all_left_right_truncatable_prime(tuple_numbers):
    x = tuple_numbers[96]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def remove_digits(n):
        return [int(str(n)[1:]), int(str(n)[:-1])]

    def is_truncatable_prime(n):
        while len(str(n)) > 2:
            n = min(remove_digits(n))
            if not is_prime(n):
                return False
        if not is_prime(n):
            return False
        return True
    primes = [i for i in range(x) if is_prime(i)]
    truncatable_primes = []
    for number in primes:
        if is_truncatable_prime(number):
            truncatable_primes.append(number)
    return sorted(truncatable_primes, reverse=True)