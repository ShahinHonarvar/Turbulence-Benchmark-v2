def all_left_truncatable_prime(t):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[35]
    if x <= 0:
        return []
    return sorted([i for i in range(2, x) if all([int(''.join(str(i)[j:])) % 5 != 0 and is_prime(int(''.join(str(i)[j:]))) for j in range(1, len(str(i)) + 1)])], reverse=True)