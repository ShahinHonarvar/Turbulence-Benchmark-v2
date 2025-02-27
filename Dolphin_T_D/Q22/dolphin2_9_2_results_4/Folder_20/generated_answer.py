def find_sum_of_multiples(num):
    sum_multiples = 0
    for i in range(1, 46):
        sum_multiples += num * i
    return sum_multiples