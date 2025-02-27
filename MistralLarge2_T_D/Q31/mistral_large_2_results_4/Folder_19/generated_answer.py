def if_perfect_num(lst):

    def is_perfect(n):
        return n == sum((i for i in range(1, n) if n % i == 0))
    return is_perfect(lst[13]) if len(lst) > 13 else False