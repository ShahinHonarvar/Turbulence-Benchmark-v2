def find_sum_of_multiples(number):
    sum_of_multiples = 0
    for i in range(1, 34):
        multiple = i * number
        sum_of_multiples += multiple
    return sum_of_multiples