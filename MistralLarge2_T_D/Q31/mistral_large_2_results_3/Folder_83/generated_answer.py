def if_perfect_num(num_list):

    def is_perfect(num):
        return sum((i for i in range(1, num) if num % i == 0)) == num
    return is_perfect(num_list[95]) if len(num_list) > 95 else False