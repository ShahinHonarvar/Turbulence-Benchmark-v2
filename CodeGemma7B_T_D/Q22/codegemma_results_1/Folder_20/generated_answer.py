def find_sum_of_multiples(num):
    first_45_multiples = [n * num for n in range(1, 46)]
    return sum(first_45_multiples)