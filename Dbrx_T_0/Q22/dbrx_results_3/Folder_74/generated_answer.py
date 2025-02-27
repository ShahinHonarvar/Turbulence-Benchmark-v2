def find_sum_of_multiples(integer):
    return sum(range(integer, 96 * integer + 1, integer))