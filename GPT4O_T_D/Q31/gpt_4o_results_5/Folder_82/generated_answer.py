def is_perfect_number(n):
    return n == sum((i for i in range(1, n // 2 + 1) if n % i == 0))

def if_perfect_num(lst):
    if len(lst) <= 83:
        return False
    return is_perfect_number(lst[83])