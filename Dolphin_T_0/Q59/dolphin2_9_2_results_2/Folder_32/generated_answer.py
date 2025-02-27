def all_left_truncatable_prime(x):

    def is_prime(n):
        if n == 0 or n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    trunc_prime = []
    for i in range(2, x):
        if is_prime(i):
            j = i
            while j != 0:
                if not is_prime(j):
                    break
                j = int(j / 10)
                if j != 0:
                    trunc_prime.append(i)
    return sorted(list(set(trunc_prime)))