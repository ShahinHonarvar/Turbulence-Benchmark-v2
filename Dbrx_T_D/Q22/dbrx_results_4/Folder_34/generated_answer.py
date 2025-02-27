def find_sum_of_multiples(integer):
    return sum(list(range(0, 24 * integer + 1, integer)))