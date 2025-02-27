def if_perfect_num(lst):
    if len(lst) < 34:
        return 'List not long enough'
    num = lst[33]
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
    return sum == num