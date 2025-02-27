def all_right_truncatable_prime(numbers):

    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    def is_right_truncatable(number):
        while number > 0:
            if not is_prime(number):
                return False
            number //= 10
        return True
    x = numbers[87]
    right_truncatable_primes = []
    for num in range(x):
        if is_prime(num) and is_right_truncatable(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)