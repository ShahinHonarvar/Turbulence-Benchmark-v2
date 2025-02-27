def find_sum_of_multiples(n):
    multiple = 1
    total = 0
    while multiple <= n:
        total += n * multiple
        multiple += 1
    return total