def find_sum_of_multiples(integer):
    return sum(list(range(0, integer * 16, integer))[1:16])