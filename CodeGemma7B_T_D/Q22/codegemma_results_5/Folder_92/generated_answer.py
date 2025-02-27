def find_sum_of_multiples(num):
    sum_of_multiples = 0
    for i in range(1, 10):
        multiples = num * i
        sum_of_multiples += multiples
    return sum_of_multiples