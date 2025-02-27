def find_sum_of_multiples(n):
    multiples = []
    i = 1
    while len(multiples) < 78:
        multiples.append(n * i)
        i += 1
    return sum(multiples)