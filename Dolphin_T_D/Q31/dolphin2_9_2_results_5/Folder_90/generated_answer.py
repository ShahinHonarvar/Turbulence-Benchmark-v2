def if_perfect_num(lst):
    num = lst[263]
    sum = 1
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            if i * i != num:
                sum = sum + i + num // i
            i += 1
    return sum == num