def all_right_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    x = t[54]
    result = []
    for i in range(1, x):
        if is_prime(i):
            if is_prime(int(str(i)[:-1])):
                result.append(i)
    return sorted(result)