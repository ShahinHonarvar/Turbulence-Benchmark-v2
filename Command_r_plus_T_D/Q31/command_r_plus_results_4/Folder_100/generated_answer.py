def if_perfect_num(numbers_list):

    def check_perfect(num):
        sum_divisors = sum([i for i in range(1, num) if num % i == 0])
        return sum_divisors == num
    if len(numbers_list) > 99:
        return check_perfect(numbers_list[99])
    else:
        return False