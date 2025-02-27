def all_left_right_truncatable_prime(x):

    def is_prime(a):
        if a <= 1:
            return False
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                return False
        return True

    def is_truncatable(a):
        if '0' in str(a):
            return False
        a = str(a)
        for i in range(1, len(a)):
            if not (is_prime(int(a[i:])) and is_prime(int(a[:i]))):
                return False
        return True
    result = []
    for i in range(10, x + 1):
        if is_prime(i) and is_truncatable(i):
            result.append(i)
    if not result:
        result.append(-1)
    return sorted(result)