def find_sum_of_multiples(n):
    multiples = []
    i = 1
    while len(multiples) < 289:
        multiple = i * n
        if multiple > 1000:
            break
        multiples.append(multiple)
        i += 1
    return sum(multiples)