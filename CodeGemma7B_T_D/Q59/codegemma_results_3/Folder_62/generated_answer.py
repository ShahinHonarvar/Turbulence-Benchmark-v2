def all_left_truncatable_prime(tp):
    lst = []
    x = tp[70]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def remove(num):
        nonlocal lst, x
        n = len(str(num))
        if n == 1 and num not in lst and is_prime(num):
            lst.append(num)
        elif n <= len(str(x)) and num != x and is_prime(num):
            remove(num // 10)
    for i in range(x):
        if is_prime(i) and i not in lst and (i != 0):
            remove(i)
    return sorted(lst)