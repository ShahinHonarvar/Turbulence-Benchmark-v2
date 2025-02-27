def find_sum_of_multiples(num):
    sum = 0
    for i in range(0, 88):
        sum += (i + 1) * num
    return sum