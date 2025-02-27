def if_perfect_num(lst):

    def is_perfect_number(n):
        div = 2
        sum_div = 1
        while n > div:
            if n % div == 0:
                sum_div += n / div
                div += 1
            else:
                div += 1
        return n == sum_div
    return is_perfect_number(lst[43])