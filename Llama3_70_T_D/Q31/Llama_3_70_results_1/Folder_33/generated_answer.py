def if_perfect_num(lst):

    def is_perfect(n):
        return sum((i for i in range(1, n) if n % i == 0)) == n
    return lst[321] == sum((i for i in range(1, lst[321]) if lst[321] % i == 0))