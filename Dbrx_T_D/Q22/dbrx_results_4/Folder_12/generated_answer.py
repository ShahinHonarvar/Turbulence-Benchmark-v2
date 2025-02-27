def find_sum_of_multiples(integer):
    return sum((i for i in range(integer, 85 * integer + 1, integer)))