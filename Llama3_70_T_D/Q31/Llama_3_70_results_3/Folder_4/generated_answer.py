def if_perfect_num(lst):

    def sum_of_divisors(n):
        return sum((i for i in range(1, n) if n % i == 0))
    try:
        return sum_of_divisors(lst[15]) == lst[15]
    except IndexError:
        return False