def if_perfect_num(lst):
    num = lst[126]
    sum = 1
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        elif i * (num // i) == num:
            sum = sum + i + num // i
            i += 1
        else:
            sum = sum + i
            i += 1
    return sum == num and len(lst) > 126