def if_perfect_num(lst):

    def is_perfect(n):
        s = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            elif i * (n // i) == n:
                s = s + i
                i += 1
            else:
                s = s + i + n // i
                i += 1
        return s == n and n != 1
    if len(lst) > 48:
        return is_perfect(lst[48])
    else:
        return False