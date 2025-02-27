def if_perfect_num(lst):
    number = lst[40]
    summation = 0
    for i in range(1, number):
        if number % i == 0:
            summation += i
    return summation == number