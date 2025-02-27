def if_perfect_num(numbers_list):

    def is_perfect(num):
        sum_divisors = sum([i for i in range(1, num) if num % i == 0])
        return sum_divisors == num
    if len(numbers_list) > 15:
        if is_perfect(numbers_list[15]):
            return True
        else:
            return False
    else:
        return False