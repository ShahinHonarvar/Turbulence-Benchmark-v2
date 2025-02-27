def all_left_truncatable_prime(num_tuple):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0:
            return False
        if n % 3 == 0:
            return False
        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True
    x = num_tuple[758]
    result = []
    for i in range(2, x):
        if is_prime(i):
            s = str(i)
            if '0' not in s:
                if all((is_prime(int(s[j:])) for j in range(len(s) - 1))):
                    result.append(i)
    return result