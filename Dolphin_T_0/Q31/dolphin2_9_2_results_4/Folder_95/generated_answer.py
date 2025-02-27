def if_perfect_num(lst):
    n = lst[87]
    sum = 1
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        elif i * (n // i) == n:
            sum = sum + i + n // i
            i += 1
        else:
            sum += i
            i += 1
    return sum == n and n != 1