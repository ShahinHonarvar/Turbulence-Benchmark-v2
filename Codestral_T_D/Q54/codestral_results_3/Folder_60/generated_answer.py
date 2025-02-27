def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[87]
    right_trunc_primes = []
    for num in range(2, x):
        if is_prime(num):
            trunc_num = num
            while trunc_num > 0:
                if not is_prime(trunc_num):
                    break
                trunc_num //= 10
            else:
                right_trunc_primes.append(num)
    return sorted(right_trunc_primes)