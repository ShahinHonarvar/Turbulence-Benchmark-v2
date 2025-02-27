def is_perfect(n):
    return n == sum((i for i in range(1, n) if n % i == 0))

def if_perfect_num(lst):
    return is_perfect(lst[28]) if len(lst) > 28 else False