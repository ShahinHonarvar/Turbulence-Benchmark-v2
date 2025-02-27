def if_perfect_num(lst):
    num = lst[54]
    sum_divs = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            sum_divs += i
    return sum_divs == num