def if_perfect_num(lst):

    def is_perfect_number(n):
        sum_of_divisors = sum((i for i in range(1, n) if n % i == 0))
        return sum_of_divisors == n
    if len(lst) > 56:
        return is_perfect_number(lst[56])
    return False