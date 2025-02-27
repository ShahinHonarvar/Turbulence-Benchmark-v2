def find_sum_of_multiples(positive_integer):
    return sum(range(positive_integer, 279 * positive_integer + 1, positive_integer))