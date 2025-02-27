def find_sum_of_multiples(i):
    sum_of_multiples = 0
    for n in range(1, 276):
        sum_of_multiples += n * i
    return sum_of_multiples