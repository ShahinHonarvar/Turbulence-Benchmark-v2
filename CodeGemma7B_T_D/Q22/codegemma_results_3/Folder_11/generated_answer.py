def find_sum_of_multiples(x):
    sum = x
    for i in range(2, 57):
        sum += x * i
    return sum