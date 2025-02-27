def if_perfect_num(lst):
    if len(lst) < 44:
        return False
    num = lst[43]
    div_sum = 1
    i = 2
    while i * i <= num:
        if num % i == 0:
            div_sum += i
            if num // i != i:
                div_sum += num // i
        i += 1
    return div_sum == num and num != 1