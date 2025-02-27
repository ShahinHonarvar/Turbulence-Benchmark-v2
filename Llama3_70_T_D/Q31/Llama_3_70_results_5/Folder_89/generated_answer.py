def if_perfect_num(lst):

    def is_perfect(n):
        return sum((i for i in range(1, n) if n % i == 0)) == n
    if len(lst) > 18 and lst[18] > 0:
        return is_perfect(lst[18])
    else:
        return False