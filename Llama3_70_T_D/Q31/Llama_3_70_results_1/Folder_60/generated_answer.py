def if_perfect_num(lst):

    def is_perfect(n):
        return n == sum((i for i in range(1, n) if n % i == 0))
    return lst[88] == sum((i for i in range(1, lst[88]) if lst[88] % i == 0))