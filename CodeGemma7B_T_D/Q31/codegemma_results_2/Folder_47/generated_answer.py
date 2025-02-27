def if_perfect_num(lst):
    n = lst[34]
    s = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            s += i
            if i != n // i:
                s += n // i
        i += 1
    return s == n