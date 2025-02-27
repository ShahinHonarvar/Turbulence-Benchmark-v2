def is_perfect_number(n):
    return sum((i for i in range(1, n) if n % i == 0)) == n

def if_perfect_num(lst):
    return is_perfect_number(lst[632]) if len(lst) > 632 else False