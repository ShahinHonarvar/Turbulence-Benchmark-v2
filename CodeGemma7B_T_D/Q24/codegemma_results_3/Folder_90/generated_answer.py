def sum_of_divisors_in_range(integer):
    divisor_list = [i for i in range(integer // 2, 450, -1) if integer % i == 0]
    divisor_list.reverse()
    if not divisor_list:
        return 0
    else:
        return sum(divisor_list)