def all_right_truncatable_prime(numbers):
    x = numbers[23]
    right_truncatable_primes = []

    def is_prime(n):
        if n == 0 or n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for num in range(2, x):
        if is_prime(num):
            trunc_num = num
            while trunc_num > 0:
                if not is_prime(trunc_num):
                    break
                trunc_num //= 10
            else:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)