def find_sum_of_multiples(positive_integer):
    return sum(list(range(0, 223 * positive_integer + 1, positive_integer)))