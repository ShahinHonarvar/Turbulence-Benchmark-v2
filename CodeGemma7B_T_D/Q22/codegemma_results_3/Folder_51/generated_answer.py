def find_sum_of_multiples(num):
    sum = 0
    for i in range(84):
        sum += (i + 1) * num
    return sum