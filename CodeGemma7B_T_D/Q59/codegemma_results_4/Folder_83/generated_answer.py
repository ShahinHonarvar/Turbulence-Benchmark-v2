def all_left_truncatable_prime(x):

    def is_prime(n):
        if n <= 2:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def left_trunc(n):
        if '0' in str(n):
            return False
        if not is_prime(n):
            return False
        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[i:])):
                return False
        return True
    sum = []
    for i in range(1, x):
        if left_trunc(i):
            sum.append(i)
    return sorted(sum)