def if_perfect_num(lst):

    def is_perfect_number(n):
        return n == sum((i for i in range(1, n) if n % i == 0))
    try:
        return is_perfect_number(lst[312])
    except IndexError:
        return False