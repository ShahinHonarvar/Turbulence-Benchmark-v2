def if_perfect_num(lst):

    def sum_divisors(n):
        return sum((i for i in range(1, n) if n % i == 0))
    try:
        if sum_divisors(lst[685]) == lst[685]:
            return True
        else:
            return False
    except IndexError:
        return False