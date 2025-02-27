def if_perfect_num(lst):
    num = lst[51]
    sum_div = 1
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            while num % i == 0:
                sum_div += i
                num //= i
            i += 1
    if num > 1:
        sum_div += num
    if sum_div == num:
        return True
    return False