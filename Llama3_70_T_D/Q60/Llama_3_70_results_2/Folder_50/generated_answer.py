def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncatable(n):
        num_str = str(n)
        if '0' in num_str:
            return False
        for i in range(len(num_str) - 1):
            if not is_prime(int(num_str[i + 1:])) or not is_prime(int(num_str[:len(num_str) - i - 1])):
                return False
        return True
    x = numbers[57]
    primes = [i for i in range(2, x + 1) if is_prime(i) and truncatable(i)]
    return sorted(primes, reverse=True)