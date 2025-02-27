def if_perfect_num(lst):
    num = lst[56]
    sum = 1
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        elif num % i == 0:
            if i * (num // i) == num:
                sum = sum + i + num // i
            else:
                sum = sum + i
            i += 1
    return sum == num and num != 1