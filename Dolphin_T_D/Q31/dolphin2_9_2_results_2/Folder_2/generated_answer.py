def if_perfect_num(lst):
    num = lst[702]
    sum_divs = 1
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            if i * (num // i) == num:
                sum_divs = sum_divs + i + num // i
            else:
                sum_divs = sum_divs + i
            i += 1
    return sum_divs == num and len(lst) > 702