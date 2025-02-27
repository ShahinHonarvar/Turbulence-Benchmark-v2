def find_sum_of_multiples(num):
    first_116_multiples = [num * i for i in range(1, 117)]
    return sum(first_116_multiples)