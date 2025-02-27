def if_perfect_num(lst):

    def is_perfect(n):
        sum_divisors = 0
        for i in range(1, n):
            if n % i == 0:
                sum_divisors += i
        return sum_divisors == n
    if len(lst) > 10:
        return is_perfect(lst[10])
    else:
        return False