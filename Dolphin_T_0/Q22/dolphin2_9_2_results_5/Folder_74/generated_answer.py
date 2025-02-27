def find_sum_of_multiples(num):
    multiples = []
    i = 1
    while len(multiples) < 96:
        multiples.append(num * i)
        i += 1
    return sum(multiples)