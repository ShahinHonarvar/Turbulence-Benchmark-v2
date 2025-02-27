def find_sum_of_multiples(integer):
    return sum(range(integer, 289 * integer + 1, integer))