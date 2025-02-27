def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        if len(str(n)) == 1:
            return is_prime(n)
        if not is_prime(n):
            return False
        return is_right_truncatable(int(str(n)[-1]))
    x = numbers[975]
    return sorted([n for n in range(2, x) if is_right_truncatable(n)], reverse=True)