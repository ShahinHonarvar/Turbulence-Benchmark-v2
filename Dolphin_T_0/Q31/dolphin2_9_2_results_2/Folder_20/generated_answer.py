def if_perfect_num(lst):

    def is_perfect(num):
        if num < 1:
            return False
        else:
            sum_div = 0
            for i in range(1, num):
                if num % i == 0:
                    sum_div += i
            return sum_div == num
    if 53 < len(lst):
        return is_perfect(lst[53])
    else:
        return False