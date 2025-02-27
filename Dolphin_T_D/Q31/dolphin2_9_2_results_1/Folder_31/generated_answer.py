def if_perfect_num(lst):
    num = lst[66]
    sum = 1
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            if i * (num // i) == num:
                sum += i
            else:
                sum += i + num // i
            i += 1
    return sum == num and num != 1