def all_right_truncable_prime(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_right_truncatable(num):
        if len(str(num)) < 2:
            return True
        return is_prime(int(str(num)[1:])) and is_right_truncatable(int(str(num)[1:]))
    x = numbers[37]
    primes = []
    for num in range(x, 1, -1):
        if is_prime(num) and is_right_truncatable(num):
            primes.append(num)
    return primes