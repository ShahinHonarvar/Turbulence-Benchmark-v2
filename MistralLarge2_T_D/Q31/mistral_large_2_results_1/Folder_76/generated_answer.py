def if_perfect_num(lst):

    def is_perfect(n):
        sum_factors = sum((i for i in range(1, n) if n % i == 0))
        return sum_factors == n
    if len(lst) > 537:
        return is_perfect(lst[537])
    return False