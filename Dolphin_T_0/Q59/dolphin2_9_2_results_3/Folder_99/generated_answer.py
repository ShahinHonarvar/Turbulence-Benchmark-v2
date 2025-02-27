def all_left_truncatable_prime(t):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n < 2:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    x = t[758]
    result = []
    for num in range(2, x):
        if all((is_prime(int(str(num)[i:])) for i in range(len(str(num)) - 1))):
            result.append(num)
    return sorted(result)