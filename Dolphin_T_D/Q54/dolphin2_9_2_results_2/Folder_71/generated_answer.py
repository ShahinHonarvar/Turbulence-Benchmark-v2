def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if not n % i:
                return False
        return True

    def is_right_truncatable(n):
        while n:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = numbers[2]
    right_truncatables = [i for i in range(x) if is_prime(i) and is_right_truncatable(i)]
    return sorted(right_truncatables, reverse=True)