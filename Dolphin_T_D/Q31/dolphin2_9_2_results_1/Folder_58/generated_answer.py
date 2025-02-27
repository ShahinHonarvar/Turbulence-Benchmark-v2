def if_perfect_num(lst):

    def is_perfect_number(num):
        sum_factors = 1
        for i in range(2, num):
            if num % i == 0:
                sum_factors += i
        return sum_factors == num
    return is_perfect_number(lst[714])