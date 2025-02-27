def find_sum_of_multiples(integer):
    sum = 0
    counter = 0
    while counter < 206:
        sum += counter * integer
        counter += 1
    return sum