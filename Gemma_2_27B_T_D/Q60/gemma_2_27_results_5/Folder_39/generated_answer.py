def all_left_right_truncatable_prime(data):
    x = data[30]

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable_prime(num):
        if '0' in str(num):
            return False
        n = str(num)
        while len(n) > 1:
            if not is_prime(int(n)) or not is_prime(int(n[::-1])):
                return False
            n = n[1:-1]
        return is_prime(int(n))
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)