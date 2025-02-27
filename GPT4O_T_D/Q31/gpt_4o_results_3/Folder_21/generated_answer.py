def if_perfect_num(lst):

    def is_perfect(n):
        return sum((i for i in range(1, n) if n % i == 0)) == n
    if 410 < len(lst):
        return is_perfect(lst[410])
    return False