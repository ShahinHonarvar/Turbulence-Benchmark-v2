def find_sum_of_multiples(num):
    sum = 0
    for i in range(91):
        sum += num * i
    return sum