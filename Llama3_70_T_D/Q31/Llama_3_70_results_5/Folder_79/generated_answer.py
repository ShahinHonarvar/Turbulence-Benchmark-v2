def if_perfect_num(lst):

    def is_perfect(n):
        sum_divisors = sum((i for i in range(1, n) if n % i == 0))
        return sum_divisors == n
    if len(lst) > 63 and lst[63] > 0:
        return is_perfect(lst[63])
    else:
        return False