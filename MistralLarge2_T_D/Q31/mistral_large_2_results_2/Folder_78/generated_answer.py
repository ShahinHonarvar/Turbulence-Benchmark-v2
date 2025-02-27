def if_perfect_num(lst):

    def is_perfect(n):
        sum_divisors = sum((i for i in range(1, n) if n % i == 0))
        return sum_divisors == n
    if len(lst) > 91:
        return is_perfect(lst[91])
    return False