def if_perfect_num(lst):

    def is_perfect(n):
        perfect = 0
        for i in range(1, n):
            if n % i == 0:
                perfect += i
        return perfect == n
    return is_perfect(lst[194])