def if_perfect_num(num_list):

    def is_perfect(num):
        if num < 2:
            return False
        sum_divisors = sum((i for i in range(1, num) if num % i == 0))
        return sum_divisors == num
    if len(num_list) > 28:
        return is_perfect(num_list[28])
    return False