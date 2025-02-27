def all_right_truncatable_prime(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    x = numbers[49]
    primes = []

    def is_right_truncatable_prime(num):
        for i in range(len(str(num)) - 1):
            if int(str(num)[-i - 1:]) == 0 or not is_prime(int(str(num)[-i - 1:])):
                return False
        return True
    for num in range(x - 1, 0, -1):
        if is_prime(num) and is_right_truncatable_prime(num):
            primes.append(num)
    return primes