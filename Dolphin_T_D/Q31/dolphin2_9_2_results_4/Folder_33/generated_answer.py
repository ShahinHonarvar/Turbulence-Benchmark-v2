def if_perfect_num(lst):

    def is_perfect(n):
        return sum((1 for i in range(1, n) if n % i == 0)) == n
    return is_perfect(lst[321]) if 321 < len(lst) else False