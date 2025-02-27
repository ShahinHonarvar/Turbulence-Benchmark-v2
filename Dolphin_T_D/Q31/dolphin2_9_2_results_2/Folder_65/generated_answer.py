def if_perfect_num(lst):
    num = lst[35]
    sum = 1
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            if num % (i * i):
                sum += i
            i += 1
    return sum == num and num != 1