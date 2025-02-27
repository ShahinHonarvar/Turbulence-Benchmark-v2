def all_left_right_truncatable_prime(numbers):
    x = numbers[30]
    primes = set()
    truncatable_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, x + 1):
        if is_prime(i):
            primes.add(i)
    for i in range(10, x + 1):
        if '0' in str(i):
            continue
        left_right_truncatable = True
        num_str = str(i)
        for j in range(1, len(num_str)):
            left_trunc = int(num_str[j:])
            right_trunc = int(num_str[:-j])
            if left_trunc not in primes or right_trunc not in primes:
                left_right_truncatable = False
                break
        if left_right_truncatable and is_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)