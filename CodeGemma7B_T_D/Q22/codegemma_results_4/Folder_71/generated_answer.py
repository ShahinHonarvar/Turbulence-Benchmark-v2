def find_sum_of_multiples(number):
    sum = 0
    for i in range(16):
        sum += number * (i + 1)
    return sum