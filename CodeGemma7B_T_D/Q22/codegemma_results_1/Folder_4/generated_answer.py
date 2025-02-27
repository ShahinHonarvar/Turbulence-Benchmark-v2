def find_sum_of_multiples(number):
    sum = 0
    multiple = number
    for i in range(40):
        sum += multiple
        multiple += number
    return sum