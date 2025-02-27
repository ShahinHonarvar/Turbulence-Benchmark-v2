def find_sum_of_multiples(num):
    sum = 0
    i = 0
    while i <= 338:
        multiples = num * i
        sum += multiples
        i += 1
    return sum