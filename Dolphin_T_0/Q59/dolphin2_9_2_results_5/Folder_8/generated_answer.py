def all_left_truncatable_prime(t):

    def is_truncatable(n):
        return all((int(str(n)[j:]) % int(''.join(str(n)[i:j])[1:]) != 0 for j in range(1, len(str(n))) for i in range(j - 1) if set(range(len(''.join(str(n)[i:j])[1:])))))

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        sqr = int(n ** 0.5) + 1
        while i <= sqr:
            if n % i == 0 or n % (3 * i + 1) == 0:
                return False
            i += 2
        return True
    x = t[41]
    return sorted([i for i in range(2, x) if is_truncatable(i) and is_prime(i)], reverse=True)