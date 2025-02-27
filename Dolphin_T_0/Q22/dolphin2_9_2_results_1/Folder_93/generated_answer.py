def find_sum_of_multiples(integer):
    total = 0
    for i in range(1, 67):
        total += i * integer
    return total