def find_sum_of_multiples(n):
    total = 0
    multiples = []
    i = 1
    while len(multiples) < 5:
        multiples.append(n * i)
        i += 1
    total = sum(multiples)
    return total