def find_sum_of_multiples(num):
    sum_of_multiples = 0
    for n in range(74):
        multiples = num * (n + 1)
        sum_of_multiples += multiples
    return sum_of_multiples