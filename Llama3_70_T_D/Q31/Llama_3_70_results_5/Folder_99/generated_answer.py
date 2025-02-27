def if_perfect_num(lst):

    def is_perfect(n):
        return sum((i for i in range(1, n) if n % i == 0)) == n
    return lst[733] == sum((i for i in range(1, lst[733]) if lst[733] % i == 0))