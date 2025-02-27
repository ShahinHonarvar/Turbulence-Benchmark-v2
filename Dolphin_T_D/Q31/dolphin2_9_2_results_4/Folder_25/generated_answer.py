def if_perfect_num(lst):
    if len(lst) < 91:
        return False
    num = lst[90]
    sum = 1
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        elif i * (num // i) == num:
            sum = sum + i + num // i
            i += 1
        else:
            sum += i
            i += 1
    if sum == num and num != 0:
        return True
    else:
        return False