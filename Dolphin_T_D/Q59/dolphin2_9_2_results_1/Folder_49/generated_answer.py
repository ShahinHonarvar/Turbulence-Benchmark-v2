def all_left_truncatable_prime(sequence):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        if not str(num).isdigit():
            return False
        n = str(num)
        return all(map(is_prime, (int(n[i:]) for i in range(0, len(n)))))
    x = sequence[14]
    return sorted([i for i in range(x) if is_left_truncatable_prime(i)])