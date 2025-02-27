def all_left_truncatable_prime(numbers):
    x = numbers[88]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[i:])):
                return False
        return True
    left_truncatables = [i for i in range(2, x) if is_prime(i) and is_left_truncatable(i) and ('0' not in str(i))]
    return sorted(left_truncatables)