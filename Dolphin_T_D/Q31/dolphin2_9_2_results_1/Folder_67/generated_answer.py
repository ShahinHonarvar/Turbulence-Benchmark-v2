def if_perfect_num(lst):

    def if_perfect(n):
        return sum((i for i in range(1, int(n ** 0.5) + 1) if n % i == 0)) * 2 == n
    return if_perfect(lst[42])