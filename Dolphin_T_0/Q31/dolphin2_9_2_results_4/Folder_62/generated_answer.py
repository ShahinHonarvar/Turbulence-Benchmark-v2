def if_perfect_num(lst):

    def is_perfect(n):
        return sum((1 for i in range(1, int(n ** 0.5) + 1) if n % i == 0)) == n - 1
    return is_perfect(lst[926])