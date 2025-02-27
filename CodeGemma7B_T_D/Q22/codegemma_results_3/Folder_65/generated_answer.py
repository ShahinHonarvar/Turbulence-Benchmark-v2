def find_sum_of_multiples(n):
    multiples = []
    current_multiple = 0
    while len(multiples) < 80:
        current_multiple += n
        if current_multiple % 2 == 0 or current_multiple % 3 == 0:
            multiples.append(current_multiple)
    return sum(multiples)