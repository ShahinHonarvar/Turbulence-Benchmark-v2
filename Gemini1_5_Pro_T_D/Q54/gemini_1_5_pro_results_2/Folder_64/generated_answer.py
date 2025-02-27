def all_right_truncatable_prime(numbers):
    x = numbers[4]

    def is_right_truncatable_prime(n):
        if n < 2:
            return False
        for i in range(len(str(n))):
            if not all([int(str(n)[:j]) > 1 and all([int(str(n)[:j]) % k for k in range(2, int(int(str(n)[:j]) ** 0.5) + 1)]) for j in range(i + 1, len(str(n)) + 1)]):
                return False
        return True
    result = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            result.append(i)
    return sorted(result)