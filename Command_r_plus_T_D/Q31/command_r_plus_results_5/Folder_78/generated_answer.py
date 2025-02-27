def if_perfect_num(numbers_list):

    def check_perfect(num):
        sum_divisors = sum([i for i in range(1, num) if num % i == 0])
        return num == sum_divisors
    if len(numbers_list) > 91:
        return check_perfect(numbers_list[91])
    else:
        return False