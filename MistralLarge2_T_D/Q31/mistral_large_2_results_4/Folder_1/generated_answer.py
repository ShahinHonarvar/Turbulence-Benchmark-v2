def if_perfect_num(lst):

    def is_perfect(n):
        if n < 1:
            return False
        sum_of_divisors = sum((i for i in range(1, n) if n % i == 0))
        return sum_of_divisors == n
    if len(lst) > 85:
        return is_perfect(lst[85])
    return False