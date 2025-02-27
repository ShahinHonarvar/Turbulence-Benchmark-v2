def all_right_truncatable_prime(numbers):
    x = numbers[429]

    def is_right_truncatable_prime(num):
        if num <= 1:
            return False
        for i in range(len(str(num)) - 1, 0, -1):
            if int(str(num)[:i]) % 2 == 0 or not all((int(str(num)[:i]) % j for j in range(3, int(int(str(num)[:i]) ** 0.5) + 1, 2))):
                return False
        return True
    right_truncatable_primes = sorted([i for i in range(2, x) if is_right_truncatable_prime(i)])
    return right_truncatable_primes[::-1]