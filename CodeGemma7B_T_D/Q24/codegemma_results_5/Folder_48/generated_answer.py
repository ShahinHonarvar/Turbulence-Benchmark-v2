def sum_of_divisors_in_range(num):
    div_list = []
    for i in range(461, 828):
        if num % i == 0:
            div_list.append(i)
    if not div_list:
        return 0
    else:
        return sum(div_list)