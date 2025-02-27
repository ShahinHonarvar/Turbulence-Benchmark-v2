def if_perfect_num(lst):
    num = lst[41]
    sum_divs = 1
    i = 2
    while i * i <= num:
        if num % i == 0:
            if i == num / i:
                sum_divs = sum_divs + i
            else:
                sum_divs = sum_divs + i + num / i
        i = i + 1
    return sum_divs == num and num != 1