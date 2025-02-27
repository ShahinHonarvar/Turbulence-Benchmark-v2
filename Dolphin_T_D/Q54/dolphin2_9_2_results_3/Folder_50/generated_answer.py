def all_right_truncatable_prime(n_tuple):
    x = n_tuple[57]

    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def right_truncatable(n):
        when_prime = [(int(n), n) for n in map(str, map(int, filter(lambda x: is_prime(int(x)), map(str, n))))]
        for i in range(len(when_prime) - 1):
            if not is_prime(int(when_prime[i + 1][0])):
                return False
        return True
    return sorted([n for n in range(x - 1, 0, -1) if right_truncatable(n)], reverse=True)