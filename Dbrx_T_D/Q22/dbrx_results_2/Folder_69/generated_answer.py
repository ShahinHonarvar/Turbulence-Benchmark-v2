def find_sum_of_multiples(positive_integer):
    sum_of_multiples = 0
    for i in range(1, 473):
        sum_of_multiples += i * positive_integer
    return sum_of_multiples