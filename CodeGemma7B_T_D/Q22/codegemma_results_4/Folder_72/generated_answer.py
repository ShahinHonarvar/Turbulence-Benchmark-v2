def find_sum_of_multiples(num):
    sum_multiples = 0
    for i in range(1, 88):
        multiple = i * num
        sum_multiples += multiple
    return sum_multiples