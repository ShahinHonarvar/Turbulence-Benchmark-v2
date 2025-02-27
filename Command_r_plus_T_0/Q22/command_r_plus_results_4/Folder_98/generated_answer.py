def find_sum_of_multiples(num):
    sum_multiples = sum((num * i for i in range(1, 11)))
    return sum_multiples