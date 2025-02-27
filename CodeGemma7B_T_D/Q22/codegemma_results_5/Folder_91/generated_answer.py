def find_sum_of_multiples(num):
    sum_of_multiples = 0
    multiples = []
    for i in range(1, 7):
        multiple = num * i
        multiples.append(multiple)
    for multiple in multiples:
        sum_of_multiples += multiple
    return sum_of_multiples