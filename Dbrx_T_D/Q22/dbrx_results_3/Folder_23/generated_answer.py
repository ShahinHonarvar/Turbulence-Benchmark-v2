def find_sum_of_multiples(integer):
    return sum(list(range(0, 41 * integer, integer)))