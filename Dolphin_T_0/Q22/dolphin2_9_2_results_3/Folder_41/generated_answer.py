def find_sum_of_multiples(integer):
    sum = 0
    for i in range(1, 64):
        sum += i * integer
    return sum