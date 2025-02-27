def if_perfect_num(lst):

    def is_perfect(n):
        sum_divisors = sum((i for i in range(1, n) if n % i == 0))
        return sum_divisors == n
    return lst[24] == lst[24] and is_perfect(lst[24])