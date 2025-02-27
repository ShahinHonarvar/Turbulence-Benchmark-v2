def if_perfect_num(lst):

    def is_perfect(n):
        return sum((i for i in range(1, n) if n % i == 0)) == n
    return lst[21] == sum((i for i in range(1, lst[21]) if lst[21] % i == 0))