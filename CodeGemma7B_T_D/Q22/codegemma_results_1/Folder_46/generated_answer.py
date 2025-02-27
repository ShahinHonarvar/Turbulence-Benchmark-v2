def find_sum_of_multiples(num):
    sum = 0
    for i in range(1, 465):
        multiple = i * num
        sum += multiple
    return sum