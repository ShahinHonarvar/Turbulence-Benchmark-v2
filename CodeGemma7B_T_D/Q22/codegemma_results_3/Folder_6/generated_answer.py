def find_sum_of_multiples(num):
    sum = 0
    for i in range(1, 475 * num, num):
        sum = sum + i
    return sum