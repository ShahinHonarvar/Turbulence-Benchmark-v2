def find_sum_of_multiples(num):
    sum_of_multiples = 0
    for i in range(1, 88):
        if i % num == 0:
            sum_of_multiples += i
    return sum_of_multiples