def find_sum_of_multiples(x):
    sum = 0
    for number in range(1, 132):
        current_multiple = number * x
        sum += current_multiple
    return sum