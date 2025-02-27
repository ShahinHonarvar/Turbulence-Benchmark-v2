def find_sum_of_multiples(value):
    sum_of_multiples = 0
    for i in range(1, 224):
        sum_of_multiples += i * value
    return sum_of_multiples