def find_sum_of_multiples(n):
    if n < 1:
        return 0
    multiples = []
    i = 1
    while len(multiples) < 40:
        multiples.append(i * n)
        i += 1
    return sum(multiples)