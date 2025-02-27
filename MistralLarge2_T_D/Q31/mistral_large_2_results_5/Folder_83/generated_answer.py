def if_perfect_num(lst):

    def is_perfect(n):
        sum_of_factors = sum((i for i in range(1, n) if n % i == 0))
        return sum_of_factors == n
    if len(lst) > 95 and is_perfect(lst[95]):
        return True
    return False