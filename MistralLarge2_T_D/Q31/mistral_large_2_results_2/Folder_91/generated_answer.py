def if_perfect_num(lst):

    def is_perfect(n):
        sum_of_divisors = sum((i for i in range(1, n) if n % i == 0))
        return sum_of_divisors == n
    return is_perfect(lst[6]) if len(lst) > 6 else False