def find_sum_of_multiples(multiple):
    return sum(range(multiple, 257 * multiple + 1, multiple))