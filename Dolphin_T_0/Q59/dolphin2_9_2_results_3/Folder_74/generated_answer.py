def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        s = int(n ** 0.5) + 1
        for i in range(3, s, 2):
            if n % i == 0:
                return False
        return True
    x = t[36]
    num_list = [i for i in range(x) if is_prime(i) and str(i).count('0') == 0]
    return sorted([i for i in num_list if all((is_prime(int(str(i)[j:])) for j in range(len(str(i)))))])