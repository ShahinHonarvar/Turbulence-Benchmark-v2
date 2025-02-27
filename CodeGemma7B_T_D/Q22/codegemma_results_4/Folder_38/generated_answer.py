def find_sum_of_multiples(num):
    multiple = 0
    total_sum = 0
    for i in range(1, 78):
        multiple = i * num
        total_sum += multiple
    return total_sum