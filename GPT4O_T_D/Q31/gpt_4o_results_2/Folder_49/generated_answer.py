def if_perfect_num(lst):
    if len(lst) <= 68:
        return False
    n = lst[68]
    return n == sum((i for i in range(1, n) if n % i == 0))