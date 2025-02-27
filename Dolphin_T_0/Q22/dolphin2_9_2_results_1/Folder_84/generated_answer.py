def find_sum_of_multiples(n):
    result = 0
    multiple = n
    while multiple <= 131 * n:
        result += multiple
        multiple += n
    return result