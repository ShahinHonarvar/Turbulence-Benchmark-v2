def if_perfect_num(numbers_list):

    def check_perfect_num(num):
        sum_divisors = sum([i for i in range(1, num) if num % i == 0])
        return num == sum_divisors
    if len(numbers_list) > 90 and check_perfect_num(numbers_list[90]):
        return True
    else:
        return False