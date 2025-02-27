def find_sum_of_multiples(value):
    sum = 0
    for i in range(1, 89):
        sum += i * value
        i += 1
    return sum