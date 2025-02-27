def if_perfect_num(lst):

    def is_perfect(n):
        sum_of_factors = 0
        for i in range(1, n):
            if n % i == 0:
                sum_of_factors += i
        return sum_of_factors == n
    if len(lst) >= 51:
        return is_perfect(lst[51])
    else:
        return False