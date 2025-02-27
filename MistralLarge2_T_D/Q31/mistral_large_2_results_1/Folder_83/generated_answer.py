def if_perfect_num(num_list):

    def is_perfect(num):
        return num == sum((i for i in range(1, num) if num % i == 0))
    return is_perfect(num_list[95]) if len(num_list) > 95 else False