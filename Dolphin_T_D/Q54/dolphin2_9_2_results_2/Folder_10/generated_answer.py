def all_right_truncatable_prime(t):

    def check_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[38]
    right_truncatable_primes = []
    for num in range(2, x):
        if check_prime(num):
            right_trunc = num
            while right_trunc > 1:
                right_trunc //= 10
                if not check_prime(right_trunc):
                    break
            else:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)