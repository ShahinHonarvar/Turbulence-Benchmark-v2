def find_sum_of_multiples(positive_integer):
    total = 0
    for num in range(1, 207):
        total += num * positive_integer
    return total