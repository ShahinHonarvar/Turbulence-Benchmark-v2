def if_perfect_num(lst):
    if len(lst) < 29:
        return False
    num = lst[28]
    sum = 1
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            if i * (num / i) == num:
                sum = sum + i + num / i
            else:
                sum = sum + i
            i = i + 1
    return sum == num and num != 1