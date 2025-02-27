def find_sum_of_multiples(number):
    sum = 0
    for i in range(88):
        multiple = (i + 1) * number
        sum += multiple
    return sum