def find_sum_of_multiples(numerator):
    sum = 0
    for i in range(1, 84):
        sum += i * numerator
    return sum