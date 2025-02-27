def find_sum_of_multiples(num):
    sum = 0
    multiple = 0
    while multiple <= 279:
        multiple += 1
        sum += num * multiple
    return sum