def find_sum_of_multiples(number):
    sum = 0
    for i in range(472):
        multiples = (i + 1) * number
        sum += multiples
    return sum