def if_perfect_num(lst):

    def is_perfect(n):
        return sum((i for i in range(1, n) if n % i == 0)) == n
    if len(lst) > 53:
        return is_perfect(lst[53])
    else:
        return False