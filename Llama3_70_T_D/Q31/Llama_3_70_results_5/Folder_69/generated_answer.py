def if_perfect_num(num_list):

    def is_perfect(num):
        sum_div = 0
        for i in range(1, num):
            if num % i == 0:
                sum_div += i
        return sum_div == num
    try:
        return is_perfect(num_list[459])
    except IndexError:
        return False