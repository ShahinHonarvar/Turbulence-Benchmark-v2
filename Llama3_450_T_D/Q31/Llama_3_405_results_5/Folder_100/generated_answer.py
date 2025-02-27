def is_perfect(n):
    return sum((i for i in range(1, n) if n % i == 0)) == n

def if_perfect_num(lst):
    return len(lst) > 99 and is_perfect(lst[99])