def all_left_truncatable_prime(t):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if n == 1:
            return False
        n = str(n)
        for i in range(1, len(n)):
            if not is_prime(int(n[i:])):
                return False
        return all((is_prime(int(n[j:])) for j in range(len(n))))
    result = [i for i in range(2, t[88]) if is_truncatable(i)]
    return sorted(result)