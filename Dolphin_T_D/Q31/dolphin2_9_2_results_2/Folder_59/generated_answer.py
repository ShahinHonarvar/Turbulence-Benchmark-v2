def if_perfect_num(lst):
    num = lst[2]
    sum_div = 1
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            if i * i != num:
                sum_div = sum_div + i + num // i
            else:
                sum_div = sum_div + i
            i += 1
    return sum_div == num and num != 1