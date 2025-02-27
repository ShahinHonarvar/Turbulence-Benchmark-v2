def all_left_right_truncatable_prime(numbers):
    x = numbers[945]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(p):
        str_p = str(p)
        if '0' in str_p:
            return False
        for i in range(1, len(str_p)):
            if not is_prime(int(str_p[i:])) or not is_prime(int(str_p[:i])):
                return False
        return True
    primes = []
    for num in range(11, x + 1):
        if is_prime(num) and is_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)