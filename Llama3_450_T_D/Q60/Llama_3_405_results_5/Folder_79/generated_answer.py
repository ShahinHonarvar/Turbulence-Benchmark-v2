def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[91]
    truncatable_primes = []
    for num in range(10, x + 1):
        if '0' in str(num):
            continue
        truncatable = True
        num_str = str(num)
        for i in range(len(num_str)):
            if not (is_prime(int(num_str[i:])) and is_prime(int(num_str[:-i or None]))):
                truncatable = False
                break
        if truncatable and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)