def all_left_truncatable_prime(lst):

    def is_prime(n):
        if n != int(n):
            return False
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        s = 3
        while s ** 2 <= n:
            if n % s == 0:
                return False
            s += 2
        return True
    x = int(lst[100])
    left_truncatable = []
    for n in range(2, x):
        n_str = str(n)
        if '0' in n_str:
            continue
        while n_str:
            if not is_prime(int(n_str)):
                break
            n_str = n_str[1:]
        else:
            left_truncatable.append(n)
    return sorted(left_truncatable)