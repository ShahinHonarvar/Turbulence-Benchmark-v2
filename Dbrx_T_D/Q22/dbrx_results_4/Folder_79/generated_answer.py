def find_sum_of_multiples(integer):
    return sum((i for i in range(integer, 28 * integer + 1, integer)))