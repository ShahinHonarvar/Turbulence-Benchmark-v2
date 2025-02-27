def if_perfect_num(lst):

    def is_perfect(n):
        if n < 0:
            return False
        return sum((d for d in range(1, n) if n % d == 0)) == n
    if len(lst) < 70:
        return None
    return is_perfect(lst[69])