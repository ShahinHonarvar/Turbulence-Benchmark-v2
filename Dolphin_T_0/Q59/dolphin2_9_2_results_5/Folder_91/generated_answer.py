def all_left_truncatable_prime(x):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, round(pow(n, 0.5)) + 1):
            if n % i == 0:
                return False
        return True
    result = []
    for i in range(x - 1, 0, -1):
        s = str(i)
        if '0' in s:
            continue
        if all((is_prime(int(s[j:])) for j in range(len(s) - 1))):
            result.append(i)
    return sorted(result, reverse=True)