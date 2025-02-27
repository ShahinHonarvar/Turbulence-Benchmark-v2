def if_perfect_num(numbers_list):

    def is_perfect(num):
        sum_divisors = sum([i for i in range(1, num) if num % i == 0])
        return num == sum_divisors
    if len(numbers_list) > 4:
        return is_perfect(numbers_list[4])
    else:
        return False