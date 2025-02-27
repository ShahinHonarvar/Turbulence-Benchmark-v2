def find_sum_of_multiples(num):
    sum_multiples = 0
    for i in range(1, 408):
        sum_multiples += i * num
    return sum_multiples