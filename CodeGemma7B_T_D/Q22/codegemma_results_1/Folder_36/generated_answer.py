def find_sum_of_multiples(arg):
    sum_of_multiples = 0
    for x in range(1, 339):
        multiples = x * arg
        sum_of_multiples += multiples
    return sum_of_multiples