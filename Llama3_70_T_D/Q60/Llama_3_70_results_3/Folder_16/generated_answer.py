def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_right_truncatable(n):
        n = str(n)
        for i in range(1, len(n)):
            left = int(n[i:])
            right = int(n[:-i])
            if not is_prime(left) or not is_prime(right):
                return False
        return True
    x = numbers[792]
    primes = [i for i in range(2, x + 1) if is_prime(i) and '0' not in str(i)]
    return [i for i in primes if left_right_truncatable(i)]