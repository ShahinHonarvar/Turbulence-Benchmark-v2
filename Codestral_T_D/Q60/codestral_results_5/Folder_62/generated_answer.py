def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if '0' in str(n):
            return False
        temp = n
        while temp > 0:
            if not is_prime(temp):
                return False
            temp //= 10
        temp = n
        while temp > 0:
            temp %= 10 ** (len(str(temp)) - 1)
            if not is_prime(temp):
                return False
        return True
    x = numbers[70]
    trunc_primes = []
    for i in range(2, x + 1):
        if is_left_right_truncatable_prime(i):
            trunc_primes.append(i)
    return sorted(trunc_primes)