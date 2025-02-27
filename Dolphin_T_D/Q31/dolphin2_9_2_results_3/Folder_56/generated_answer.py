def if_perfect_num(list_of_integers):
    target_num = list_of_integers[60]
    sum = 1
    i = 2
    while i * i <= target_num:
        if target_num % i:
            i += 1
        elif i * (target_num // i) == target_num:
            sum = sum + i + target_num // i
            i += 1
        else:
            sum = sum + i
            i += 1
    return sum == target_num