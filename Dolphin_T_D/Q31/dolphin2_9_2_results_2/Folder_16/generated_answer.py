def if_perfect_num(lst):
    if len(lst) < 163:
        return False
    n = lst[162]
    sum = 1
    for i in range(2, n):
        if n % i == 0:
            sum += i
    return sum == n