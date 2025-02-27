def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[2]
    left_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i) and '0' not in str(i):
            trunc_i = i
            while trunc_i:
                trunc_i //= 10
                if not is_prime(trunc_i):
                    break
            else:
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)