def if_perfect_num(num_list):
    if num_list[851] > 0:
        sum_divisors = 0
        for i in range(1, num_list[851]):
            if num_list[851] % i == 0:
                sum_divisors += i
        if sum_divisors == num_list[851]:
            return True
    return False