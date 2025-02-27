def find_sum_of_multiples(n):
    sum_of_multiples = 0
    for i in range(21):
        multiple = i * n
        sum_of_multiples += multiple
    return sum_of_multiples