def if_perfect_num(lst):
    if len(lst) < 58:
        raise ValueError('List does not contain 57 elements')
    num = lst[57]
    sum = 1
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        elif i * (num // i) == num:
            sum = sum + i + num // i
            i += 1
        else:
            sum += i
            i += 1
    return sum == num