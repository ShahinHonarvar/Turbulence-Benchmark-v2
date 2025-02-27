def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_truncatable(n):
        num_str = str(n)
        for i in range(1, len(num_str)):
            if not is_prime(int(num_str[i:])):
                return False
        return True
    x = numbers[758]
    primes = [i for i in range(2, x) if is_prime(i) and '0' not in str(i) and left_truncatable(i)]
    return sorted(primes)