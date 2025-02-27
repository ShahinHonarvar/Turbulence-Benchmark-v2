def if_perfect_num(lst):

    def is_perfect(n):
        return n == sum([i for i in range(1, n) if n % i == 0])
    if len(lst) > 45:
        return is_perfect(lst[45])
    return False