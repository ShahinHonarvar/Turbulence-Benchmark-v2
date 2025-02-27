def if_perfect_num(lst):

    def is_perfect(num):
        sum_div = 1
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            elif i * (num // i) == num:
                sum_div = sum_div + i + num // i
                i += 1
            else:
                sum_div = sum_div + i
                i += 1
        return sum_div == num and num != 1
    if len(lst) > 41:
        return is_perfect(lst[41])
    else:
        raise ValueError('The list is too short.')