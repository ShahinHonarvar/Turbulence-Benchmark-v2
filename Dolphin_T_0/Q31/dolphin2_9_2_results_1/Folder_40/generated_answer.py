def if_perfect_num(lst):
    number = lst[7]
    sum_div = 1
    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        else:
            if i * (number // i) == number:
                sum_div = sum_div + i + number // i
            else:
                sum_div = sum_div + i
            i += 1
    return sum_div == number and number != 1