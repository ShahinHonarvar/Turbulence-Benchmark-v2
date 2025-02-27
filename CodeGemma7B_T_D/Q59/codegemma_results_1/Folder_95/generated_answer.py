def all_left_truncatable_prime(t):
    t77 = t[77]
    lt = [i for i in range(11, t77) if not str(i).startswith('0') and all((p in p_list for p in str(i)))]
    return sorted([i for i in lt if left_truncatable(i)])

def left_truncatable(n):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return all((is_prime(int(str(n)[i:])) for i in range(1, len(str(n)))))