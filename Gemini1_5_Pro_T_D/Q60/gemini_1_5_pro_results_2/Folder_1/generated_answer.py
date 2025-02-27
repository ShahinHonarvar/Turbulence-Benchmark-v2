def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if not is_prime(n) or '0' in str(n):
            return False
        left, right = (str(n), str(n))
        while len(left) > 1:
            left = left[1:]
            right = right[:-1]
            if not (is_prime(int(left)) and is_prime(int(right))):
                return False
        return True
    x = numbers[20]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes