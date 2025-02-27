def if_perfect_num(lst):

    def is_perfect(n):
        return sum((i for i in range(1, n) if n % i == 0)) == n
    if len(lst) > 3 and lst[3] > 0:
        return is_perfect(lst[3])
    else:
        return False