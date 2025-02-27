def find_sum_of_multiples(n):
    multiples = []
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            multiples.append(j)
    return sum(multiples)