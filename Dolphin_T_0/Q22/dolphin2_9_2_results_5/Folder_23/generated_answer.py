def find_sum_of_multiples(num):
    sum_41_multiples = 0
    for i in range(1, 42):
        sum_41_multiples += i * num
    return sum_41_multiples