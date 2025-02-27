def all_left_right_truncatable_prime(numbers):
    x = numbers[35]

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_truncatable(num):
        num_str = str(num)
        if '0' in num_str:
            return False
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:-i or None])):
                return False
        return True
    truncatable_primes = [i for i in range(11, x + 1) if is_prime(i) and is_truncatable(i)]
    return sorted(truncatable_primes, reverse=True)