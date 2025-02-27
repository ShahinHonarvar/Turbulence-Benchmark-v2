def if_perfect_num(lst):
    num = lst[84]
    sum = 1
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            if num % (i * i) == 0:
                sum += i
            else:
                sum += i + num / i
            i += 1
    return sum == num and num != 1