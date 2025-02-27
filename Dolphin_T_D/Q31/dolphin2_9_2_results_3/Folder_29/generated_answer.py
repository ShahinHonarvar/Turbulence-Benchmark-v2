def if_perfect_num(lst):
    if len(lst) < 20:
        return False
    num = lst[19]
    sum = 1
    i = 2
    while i * i <= num:
        if num % i == 0:
            if i * i == num:
                sum = sum + i
            else:
                sum = sum + i + num / i
        i = i + 1
    return sum == num