def if_perfect_num(lst):
    if len(lst) < 78:
        return False
    num = lst[77]
    sum = 1
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            if i == num / i:
                sum = sum + i
            else:
                sum = sum + i + num / i
            i += 1
    if sum == num:
        return True
    else:
        return False