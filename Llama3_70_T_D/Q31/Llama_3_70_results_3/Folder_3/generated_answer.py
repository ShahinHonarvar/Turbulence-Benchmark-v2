def if_perfect_num(lst):

    def sum_divisors(n):
        return sum((i for i in range(1, n) if n % i == 0))
    if len(lst) > 100:
        return sum_divisors(lst[100]) == lst[100]
    else:
        return False