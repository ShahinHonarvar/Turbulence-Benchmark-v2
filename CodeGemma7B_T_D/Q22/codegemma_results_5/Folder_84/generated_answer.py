def find_sum_of_multiples(num):
    sum_of_multiples = 0
    multiple = 0
    for i in range(1, 132):
        multiple = i * num
        sum_of_multiples += multiple
    return sum_of_multiples