def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_lr_truncatable_prime(n):
        i = 10 ** (len(str(n)) - 1)
        while i > 1:
            left_number = n // i
            right_number = n % i
            if left_number == 0 or right_number == 0:
                return False
            if not is_prime(left_number) or not is_prime(right_number):
                return False
            i //= 10
        return True
    x = numbers[67]
    left_right_truncatable_primes = []
    for i in range(x, 1, -1):
        if is_lr_truncatable_prime(i):
            left_right_truncatable_primes.append(i)
    return left_right_truncatable_primes