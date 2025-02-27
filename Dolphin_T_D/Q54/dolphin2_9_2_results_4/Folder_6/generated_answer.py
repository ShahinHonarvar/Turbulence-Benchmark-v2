def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[74]
    l = [i for i in range(2, x) if is_prime(i)]
    r = list(filter(lambda n: all((is_prime(int(str(n)[i:])) for i in range(len(str(n))))) and len(str(n)) > 1, l))
    return sorted(r) if r else []