def find_sum_of_multiples(given_number):
    sum = 0
    for i in range(1, 81):
        multiples = i * given_number
        sum += multiples
    return sum