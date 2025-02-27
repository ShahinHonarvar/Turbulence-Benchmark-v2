def if_perfect_num(lst):
    num = lst[15]
    sum = 1
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            if num > i:
                sum = sum + i + num / i
            else:
                sum = sum + i
            i += 1
    if num > 1:
        return sum == num
    else:
        return False