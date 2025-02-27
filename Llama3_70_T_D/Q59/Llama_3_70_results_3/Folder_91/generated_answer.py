def all_left_truncatable_prime(n):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        num_str = str(num)
        if '0' in num_str:
            return False
        for i in range(1, len(num_str)):
            if not is_prime(int(num_str[i:])):
                return False
        return True
    x = n[0]
    primes = [i for i in range(2, x) if is_prime(i) and is_left_truncatable_prime(i)]
    return sorted(primes, reverse=True)