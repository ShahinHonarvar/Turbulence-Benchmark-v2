def if_perfect_num(lst):

    def is_perfect_number(n):
        sum_divisors = sum((i for i in range(1, n) if n % i == 0))
        return sum_divisors == n
    return is_perfect_number(lst[13]) if len(lst) > 13 else False