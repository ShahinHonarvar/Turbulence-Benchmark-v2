def if_perfect_num(lst):
    num = lst[68]
    sum = 1
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            if num % (num / i) == 0:
                sum = sum + i + num / i
            i += 1
    return num == sum and num != 1