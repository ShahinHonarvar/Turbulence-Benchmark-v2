def find_sum_of_multiples(x):
    sum = 0
    for i in range(1, 473):
        num = x * i
        sum += num
    return sum