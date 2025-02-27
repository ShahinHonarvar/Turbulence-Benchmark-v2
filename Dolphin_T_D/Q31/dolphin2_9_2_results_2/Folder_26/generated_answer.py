def if_perfect_num(lst):
    num = lst[222]
    sum = 1
    i = 2
    while i * i <= num:
        if num % i == 0:
            if i * i != num:
                sum += i
            if i != num // i:
                sum += num // i
        i += 1
    return sum == num