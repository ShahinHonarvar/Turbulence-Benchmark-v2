def is_perfect(n):
    return sum((i for i in range(1, n) if n % i == 0)) == n

def if_perfect_num(lst):
    if len(lst) > 23:
        return is_perfect(lst[23])
    else:
        return False