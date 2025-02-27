def find_sum_of_multiples(number):
    sum = 0
    for i in range(1, 6):
        sum += i * number
    return sum