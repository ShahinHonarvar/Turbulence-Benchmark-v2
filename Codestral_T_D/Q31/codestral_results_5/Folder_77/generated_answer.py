def is_perfect_num(lst):
    num = lst[985]
    sum = 1
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            if i * (num / i) == num:
                sum = sum + i + num / i
            else:
                sum = sum + i
            i += 1
    if num == sum:
        return True
    else:
        return False