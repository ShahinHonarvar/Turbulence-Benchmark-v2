def if_perfect_num(lst):
    if len(lst) < 20:
        return False
    n = lst[19]
    sum = 1
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        elif i == n // i:
            sum = sum + i
            i += 1
    return sum == n