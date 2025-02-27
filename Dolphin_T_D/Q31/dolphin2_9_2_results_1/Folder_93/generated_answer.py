def if_perfect_num(lst):
    if len(lst) < 46:
        return False
    number = lst[45]
    sum = 1
    for i in range(2, number):
        if number % i == 0:
            sum += i
    if sum == number:
        return True
    else:
        return False