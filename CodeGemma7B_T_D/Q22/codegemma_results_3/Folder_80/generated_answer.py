def find_sum_of_multiples(number):
    sum_of_multiples = 0
    for i in range(1, 277):
        sum_of_multiples += i * number
    return sum_of_multiples