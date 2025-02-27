def find_sum_of_multiples(n):
    sum_of_multiples = 0
    multiple = n
    for i in range(100):
        sum_of_multiples += multiple
        multiple += n
    return sum_of_multiples