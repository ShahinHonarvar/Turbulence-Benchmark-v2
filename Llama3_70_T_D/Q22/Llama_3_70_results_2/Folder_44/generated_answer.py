def find_sum_of_multiples(n):
    sum_of_multiples = 0
    multiple = n
    count = 0
    while count < 445:
        sum_of_multiples += multiple
        multiple += n
        count += 1
    return sum_of_multiples