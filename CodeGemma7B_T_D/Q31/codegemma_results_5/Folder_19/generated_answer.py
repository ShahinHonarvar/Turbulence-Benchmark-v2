def if_perfect_num(given_list):
    if len(given_list) >= 13:
        num = given_list[13]
        sum_of_divisors = 0
        for divisor in range(1, num):
            if num % divisor == 0:
                sum_of_divisors += divisor
        if sum_of_divisors == num:
            return True
        return False
    return None