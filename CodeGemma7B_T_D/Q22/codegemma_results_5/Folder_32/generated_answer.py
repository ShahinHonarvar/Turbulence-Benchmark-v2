def find_sum_of_multiples(num):
    result = 0
    for i in range(113):
        multiples = i * num
        result += multiples
    return result