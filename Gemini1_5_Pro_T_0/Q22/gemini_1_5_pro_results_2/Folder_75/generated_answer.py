def find_sum_of_multiples(integer):
    sum = 0
    for i in range(1, 16):
        sum += integer * i
    return sum