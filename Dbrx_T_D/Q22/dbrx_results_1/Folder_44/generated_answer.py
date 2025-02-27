def find_sum_of_multiples(positive_integer):
    return sum((positive_integer * i for i in range(1, 446)))