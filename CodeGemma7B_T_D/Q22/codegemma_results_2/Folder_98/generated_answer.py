def find_sum_of_multiples(num):
    multiple = 1
    sum = 0
    while multiple <= 10:
        sum += multiple * num
        multiple += 1
    return sum