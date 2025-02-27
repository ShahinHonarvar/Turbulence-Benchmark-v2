def find_sum_of_multiples(integer):
    return sum(range(1, 83 * integer + 1, integer))