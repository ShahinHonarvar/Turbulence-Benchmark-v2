def find_sum_of_multiples(x):
    sum_of_multiples = 0
    for i in range(1, 78):
        sum_of_multiples += i * x
    return sum_of_multiples