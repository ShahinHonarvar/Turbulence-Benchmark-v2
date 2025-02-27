def find_sum_of_multiples(num):
    sum = 0
    for count in range(1, 93):
        sum += num * count
    return sum