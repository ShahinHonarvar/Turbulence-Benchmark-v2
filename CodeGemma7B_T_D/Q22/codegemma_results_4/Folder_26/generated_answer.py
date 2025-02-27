def find_sum_of_multiples(num):
    sum_of_multiples = 0
    for multiple in range(1, 367):
        sum_of_multiples += multiple * num
    return sum_of_multiples