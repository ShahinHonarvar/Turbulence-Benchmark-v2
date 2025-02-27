def find_sum_of_multiples(n):
    multiples = []
    counter = 1
    while len(multiples) < 13:
        multiple = n * counter
        multiples.append(multiple)
        counter += 1
    return sum(multiples)