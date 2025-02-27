def find_sum_of_multiples(num):
    sum = 0
    multiple = 1
    while multiple <= 464:
        sum += multiple * num
        multiple += 1
    return sum