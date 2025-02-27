def find_sum_of_multiples(num):
    multiples = []
    for i in range(1, 29):
        multiples.append(i * num)
    return sum(multiples)