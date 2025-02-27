def find_sum_of_multiples(num):
    sum = 0
    for i in range(1, 148):
        multiples = i * num
        sum += multiples
    return sum