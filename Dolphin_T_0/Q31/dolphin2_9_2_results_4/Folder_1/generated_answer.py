def if_perfect_num(lst):
    if len(lst) < 86:
        return False
    num = lst[85]
    sum = 1
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            if num % (i * i) == i:
                sum = sum + i
            else:
                sum = sum + (i + num // i)
            i += 1
    return sum == num