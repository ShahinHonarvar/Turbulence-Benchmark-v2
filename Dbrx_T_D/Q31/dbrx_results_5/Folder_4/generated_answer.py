def if_perfect_num(number_list):
    if len(number_list) > 15:
        perfect_num = number_list[15]
        if perfect_num > 0:
            sum_divisors = 0
            for i in range(1, perfect_num):
                if perfect_num % i == 0:
                    sum_divisors += i
            if sum_divisors == perfect_num:
                return True
    return False