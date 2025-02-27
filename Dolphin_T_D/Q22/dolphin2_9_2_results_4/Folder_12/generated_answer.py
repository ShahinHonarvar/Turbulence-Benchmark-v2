def find_sum_of_multiples(num):
    sum = 0
    for i in range(1, 86):
        sum += i * num
    return sum