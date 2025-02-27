def find_sum_of_multiples(number):
    sum = 0
    for n in range(1, 42):
        sum += n * number
    return sum