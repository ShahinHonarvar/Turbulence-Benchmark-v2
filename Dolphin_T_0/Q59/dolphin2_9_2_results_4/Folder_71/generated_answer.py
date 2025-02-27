def all_left_truncatable_prime(numbers):

    def is_left_truncatable_prime(n):
        if n < 2:
            return False
        while n != 0:
            if not is_prime(n):
                return False
            n //= 10
        return True

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[22]
    numbers_less_than_x = [i for i in range(x)]
    return sorted(filter(is_left_truncatable_prime, reversed(numbers_less_than_x)), reverse=True)