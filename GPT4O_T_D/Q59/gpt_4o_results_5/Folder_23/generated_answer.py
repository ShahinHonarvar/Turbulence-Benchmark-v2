def all_left_truncatable_prime(numbers):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable(prime):
        str_prime = str(prime)
        while str_prime:
            if not is_prime(int(str_prime)):
                return False
            str_prime = str_prime[1:]
        return True
    x = numbers[77]
    left_truncatable_primes = [num for num in range(2, x) if is_left_truncatable(num)]
    return sorted(left_truncatable_primes, reverse=True)