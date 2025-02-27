def find_sum_of_multiples(positive_integer):
    sum = 0
    for i in range(1, 19):
        sum += i * positive_integer
    return sum