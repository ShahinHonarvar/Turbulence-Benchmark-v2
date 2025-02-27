def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[6]
    primes = []
    for num in range(x, 1, -1):
        if all((is_prime(int(''.join(digits))) and '0' not in digits for digit in zip(str(num), '1' + str(num)[1:]))):
            primes.append(num)
    return primes