def find_sum_of_multiples(integer):
    sum = 0
    i = 1
    while i < 44:
        sum += integer * i
        i += 1
    return sum