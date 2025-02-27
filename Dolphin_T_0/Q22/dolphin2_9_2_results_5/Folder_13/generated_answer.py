def find_sum_of_multiples(positive_integer):
    sum = 0
    for i in range(1, 207):
        sum += positive_integer * i
    return sum