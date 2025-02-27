def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        n = str(n)
        for i in range(len(n) - 1, 0, -1):
            if not is_prime(int(n[i:])) or n[i - 1] == '0':
                return False
        return True
    x = numbers[61]
    return [i for i in range(2, x) if is_prime(i) and is_left_truncatable(i)]