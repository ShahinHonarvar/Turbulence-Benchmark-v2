def find_sum_of_multiples(argument):
    sum_of_multiples = 0
    for i in range(1, 277):
        sum_of_multiples += i * argument
    return sum_of_multiples