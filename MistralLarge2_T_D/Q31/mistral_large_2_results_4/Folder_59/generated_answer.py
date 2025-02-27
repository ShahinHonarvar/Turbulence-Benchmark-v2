def if_perfect_num(lst):

    def is_perfect(n):
        sum_divisors = sum((i for i in range(1, n) if n % i == 0))
        return sum_divisors == n
    return is_perfect(lst[2]) if len(lst) > 2 else False