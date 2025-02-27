def if_perfect_num(lst):
    if len(lst) < 16:
        return False
    num = lst[15]
    sum = 1
    i = 2
    while i * i <= num:
        if num % i == 0:
            if i * i != num:
                sum = sum + i + num / i
            else:
                sum = sum + i
        i += 1
    return sum == num and num != 1