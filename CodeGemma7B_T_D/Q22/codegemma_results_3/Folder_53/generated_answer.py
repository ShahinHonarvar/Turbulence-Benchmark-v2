def find_sum_of_multiples(i):
    multiples = []
    for x in range(1, 61):
        multiples.append(i * x)
    return sum(multiples)