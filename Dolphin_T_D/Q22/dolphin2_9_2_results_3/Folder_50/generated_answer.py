def find_sum_of_multiples(n):
    sum = 0
    multiple = 1
    while multiple <= 99:
        sum += n * multiple
        multiple += 1
    return sum