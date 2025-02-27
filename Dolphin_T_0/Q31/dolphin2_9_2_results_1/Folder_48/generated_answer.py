def if_perfect_num(lst):
    if len(lst) < 248:
        return False
    num = lst[247]
    if num <= 0:
        return False
    div_sum = 0
    i = 1
    while i * i <= num:
        if num % i == 0:
            div_sum += i
            if num // i != i:
                div_sum += num // i
        i += 1
    return div_sum == num