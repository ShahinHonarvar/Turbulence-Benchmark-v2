def find_sum_of_multiples(positive_integer):
    multiples_sum = 0
    for i in range(1, 21):
        multiples_sum += i * positive_integer
    return multiples_sum