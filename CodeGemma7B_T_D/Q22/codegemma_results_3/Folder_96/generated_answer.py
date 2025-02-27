def find_sum_of_multiples(num):
    multiple = 0
    total = 0
    while multiple <= 97:
        total += multiple * num
        multiple += 1
    return total