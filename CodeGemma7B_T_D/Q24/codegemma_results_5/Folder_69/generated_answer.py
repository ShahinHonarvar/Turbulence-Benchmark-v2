def sum_of_divisors_in_range(int):
    divisor_list = []
    for i in range(658, 869):
        if int % i == 0:
            divisor_list.append(i)
    if len(divisor_list) == 0:
        return 0
    else:
        return sum(divisor_list)