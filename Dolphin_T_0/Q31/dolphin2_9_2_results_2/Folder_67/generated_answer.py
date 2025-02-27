def if_perfect_num(l):

    def is_perfect(n):
        return sum([i for i in range(1, n) if n % i == 0]) == n
    if len(l) > 43 and is_perfect(l[43]):
        return True
    return False