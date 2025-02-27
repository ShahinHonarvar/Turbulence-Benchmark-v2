def if_perfect_num(lst):

    def is_perfect(num):
        sum_of_factors = 1
        for i in range(2, num):
            if num % i == 0:
                sum_of_factors += i
        return sum_of_factors == num
    return is_perfect(lst[51]) if len(lst) > 51 else False