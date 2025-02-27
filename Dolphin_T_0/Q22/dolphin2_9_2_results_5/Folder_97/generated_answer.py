def find_sum_of_multiples(positive_integer):
    sum_of_multiples = 0
    for i in range(1, 211):
        sum_of_multiples += positive_integer * i
    return sum_of_multiples