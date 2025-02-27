def if_perfect_num(lst):

    def is_perfect(num):
        div = 1
        sum = 0
        while div < num:
            if num % div == 0:
                sum += div
            div += 1
        return sum == num
    return is_perfect(lst[2])