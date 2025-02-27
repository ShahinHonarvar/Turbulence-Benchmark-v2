def find_sum_of_multiples(num):
    multiplier = 0
    sum = 0
    while multiplier <= 444:
        if multiplier % num == 0:
            sum += multiplier
        multiplier += 1
    return sum