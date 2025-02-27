def find_sum_of_multiples(x):
    sum = 0
    for i in range(1, 48):
        sum += i * x
    return sum