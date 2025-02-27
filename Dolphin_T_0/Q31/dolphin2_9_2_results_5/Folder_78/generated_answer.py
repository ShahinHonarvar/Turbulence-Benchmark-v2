def if_perfect_num(lst):

    def is_perfect(n):
        return sum((d for d in range(1, n) if n % d == 0)) == n
    return is_perfect(lst[91])