def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def right_truncatable_prime(n):
        for i in range(len(str(n)) - 1, -1, -1):
            if not is_prime(int(str(n)[:i + 1])):
                return False
        return True
    x = numbers[87]
    return sorted([i for i in range(2, x) if right_truncatable_prime(i)])