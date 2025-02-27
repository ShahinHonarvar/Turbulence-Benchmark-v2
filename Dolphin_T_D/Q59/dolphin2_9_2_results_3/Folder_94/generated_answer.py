def all_left_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if str(n)[0] == '0':
            return False
        n = str(n)
        for i in range(len(n)):
            if not is_prime(int(n[i:])):
                return False
        return True
    x = t[43]
    result = [i for i in range(2, x) if is_truncatable(i) and is_prime(i)]
    return sorted(result)