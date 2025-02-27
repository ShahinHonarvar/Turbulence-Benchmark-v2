def find_sum_of_multiples(n):
    multiples = []
    for i in range(1, 42):
        multiple = i * n
        multiples.append(multiple)
    return sum(multiples)