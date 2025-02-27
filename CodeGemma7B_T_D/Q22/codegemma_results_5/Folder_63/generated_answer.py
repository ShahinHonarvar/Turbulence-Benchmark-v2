def find_sum_of_multiples(x):
    sum = 0
    for number in range(x, x + 18 * x, x):
        sum = sum + number
    return sum