def if_perfect_num(number_list):
    if len(number_list) > 80:
        number = number_list[80]
        sum_of_divisiors = 0
        for i in range(1, number // 2 + 1):
            if number % i == 0:
                sum_of_divisiors += i
        if sum_of_divisiors == number:
            return True
    return False