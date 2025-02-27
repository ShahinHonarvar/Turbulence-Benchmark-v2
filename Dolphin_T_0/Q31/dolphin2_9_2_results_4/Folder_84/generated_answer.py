def if_perfect_num(int_list):
    num = int_list[685]
    sum_1 = 1
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        elif i * (num // i) == num:
            sum_1 = sum_1 + i + num // i
            i += 1
        else:
            sum_1 = sum_1 + i
            i += 1
    return sum_1 == num and num != 1