def find_sum_of_multiples(n):
    multiples = [n * i for i in range(1, 189)]
    return sum(multiples)