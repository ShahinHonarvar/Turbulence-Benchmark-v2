def find_sum_of_multiples(positive_integer):
    return sum(range(1, 464 * positive_integer + 1, positive_integer))