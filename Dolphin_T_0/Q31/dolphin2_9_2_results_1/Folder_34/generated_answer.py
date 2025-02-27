def if_perfect_num(num_list):
    num = num_list[97]
    sum_div = 0
    i = 1
    while i * i < num:
        if num % i == 0:
            sum_div += i
            if i * i != num:
                sum_div += num / i
        i += 1
    return sum_div == num