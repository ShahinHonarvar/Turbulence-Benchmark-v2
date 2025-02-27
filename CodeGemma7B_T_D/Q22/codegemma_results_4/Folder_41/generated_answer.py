def find_sum_of_multiples(x):
    multiples = [x * i for i in range(1, 64)]
    return sum(multiples)