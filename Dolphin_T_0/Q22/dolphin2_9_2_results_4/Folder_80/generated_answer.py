def find_sum_of_multiples(n):
    s = 0
    i = 1
    multiples = set()
    while len(multiples) < 276:
        if i % n == 0 and i not in multiples:
            multiples.add(i)
            s += i
        i += 1
    return s