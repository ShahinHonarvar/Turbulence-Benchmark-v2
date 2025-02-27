def all_left_truncatable_prime(n):

    def is_prime(m):
        for i in range(2, int(m ** 0.5) + 1):
            if m % i == 0:
                return False
        return True
    x = n[11]
    result = []
    for i in range(2, x):
        if '0' not in str(i):
            if is_prime(i):
                if all((is_prime(int(str(i)[j:])) for j in range(1, len(str(i))))):
                    result.append(i)
    return result