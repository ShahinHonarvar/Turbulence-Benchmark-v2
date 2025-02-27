def if_perfect_num(lst):

    def is_perfect(n):
        if n == 1:
            return 1
        if n < 1:
            return 0
        return n + is_perfect(int(n - sum([i for i in range(1, int(n ** 0.5) + 1) if n % i == 0])))
    return is_perfect(lst[632])