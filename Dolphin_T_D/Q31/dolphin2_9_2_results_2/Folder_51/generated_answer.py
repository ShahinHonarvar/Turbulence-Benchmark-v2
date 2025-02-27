def if_perfect_num(lst):

    def is_perfect(n):
        return sum((1 for i in range(1, n) if n % i == 0)) == n
    if len(lst) >= 65 and is_perfect(lst[64]):
        return True
    else:
        return False