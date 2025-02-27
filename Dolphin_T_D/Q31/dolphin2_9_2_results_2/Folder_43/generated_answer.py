def if_perfect_num(lst):
    if len(lst) < 30:
        return False
    num = lst[29]
    if num < 1:
        return False
    sum = 1
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        elif i * (num // i) < num:
            sum = sum + i + num // i
            i += 1
        else:
            sum = sum + i
            i += 1
    return sum == num