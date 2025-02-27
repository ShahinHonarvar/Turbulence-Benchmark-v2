def find_sum_of_multiples(number):
    total = 0
    for x in range(1, 78):
        total += x * number
    return total