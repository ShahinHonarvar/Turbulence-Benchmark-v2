def find_sum_of_multiples(arg):
    sum = 0
    for i in range(1, 9):
        sum += i * arg
    return sum