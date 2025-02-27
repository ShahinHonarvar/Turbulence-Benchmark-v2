def if_perfect_num(numbers_list):

    def is_perfect(num):
        sum_divisors = sum([i for i in range(1, num) if num % i == 0])
        return sum_divisors == num
    if len(numbers_list) > 48:
        num_to_check = numbers_list[48]
        return is_perfect(num_to_check)
    else:
        return False