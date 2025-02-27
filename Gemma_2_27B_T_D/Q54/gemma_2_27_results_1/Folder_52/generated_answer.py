def all_right_truncatable_prime(x):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = x[52]
    result = []
    for i in range(x - 1, 0, -1):
        s = str(i)
        is_right_truncatable = True
        for j in range(len(s)):
            if not is_prime(int(s[:j + 1])):
                is_right_truncatable = False
                break
        if is_right_truncatable:
            result.append(i)
    return sorted(result, reverse=True)