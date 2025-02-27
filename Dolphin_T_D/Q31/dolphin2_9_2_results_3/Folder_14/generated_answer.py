def if_perfect_num(lst):

    def is_perfect(n):
        if n < 0:
            return False
        if n:
            return n == sum((i for i in range(1, n) if n % i == 0))
        return True
    return is_perfect(lst[17])