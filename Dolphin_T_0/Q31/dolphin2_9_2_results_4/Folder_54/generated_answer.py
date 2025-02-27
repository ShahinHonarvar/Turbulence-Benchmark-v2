def if_perfect_num(num_list):
    if len(num_list) < 52:
        return False
    num = num_list[51]
    if num < 6:
        return False
    sum = 1
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            if i * (num // i) == num:
                sum = sum + i + num // i
            else:
                sum = sum + i
            i += 1
    return sum == num