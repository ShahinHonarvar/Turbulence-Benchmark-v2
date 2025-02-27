def if_perfect_num(lst):
    num = lst[1]
    sum_div = 1
    i = 2
    while i * i <= num:
        if num % i == 0:
            if i * (num // i) == num:
                sum_div += i
            else:
                sum_div += i
                sum_div += num // i
        i += 1
    return sum_div == num