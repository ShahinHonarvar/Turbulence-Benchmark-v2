def find_sum_of_multiples(num):
    sum = 0
    for i in range(5):
        sum += num * (i + 1)
    return sum