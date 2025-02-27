def if_perfect_num(lst):

    def is_perfect(n):
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors) == n
    if len(lst) > 312:
        return is_perfect(lst[312])
    else:
        return False