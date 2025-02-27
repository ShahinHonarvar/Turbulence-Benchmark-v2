def find_sum_of_multiples(arg):
    sum = 0
    if arg > 0:
        for i in range(1, 11):
            sum += arg * i
    return sum