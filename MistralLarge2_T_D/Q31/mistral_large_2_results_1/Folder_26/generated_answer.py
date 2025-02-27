def if_perfect_num(lst):

    def is_perfect(n):
        if n < 2:
            return False
        sum_divisors = sum((i for i in range(1, n) if n % i == 0))
        return sum_divisors == n
    return is_perfect(lst[222]) if len(lst) > 222 else False