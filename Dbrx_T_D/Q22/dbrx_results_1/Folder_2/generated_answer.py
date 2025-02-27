def find_sum_of_multiples(positive_integer):
    sum = 0
    multiple = 1
    while multiple < 147:
        sum += multiple * positive_integer
        multiple += 1
    return sum