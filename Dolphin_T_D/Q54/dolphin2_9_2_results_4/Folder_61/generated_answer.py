def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        return all((is_prime(int(str(n)[-i - 1:])) for i in range(len(str(n)) - 1)))
    x = numbers[3]
    return sorted([i for i in range(2, x) if is_right_truncatable(i)], reverse=True)