def all_right_truncatable_prime(arr):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        if len(str(n)) == 1:
            return is_prime(n)
        return is_prime(n) and is_right_truncatable(n // 10)
    x = arr[11]
    primes = [i for i in range(2, x) if is_right_truncatable(i)]
    return sorted(primes)