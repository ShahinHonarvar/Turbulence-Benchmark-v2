def find_sum_of_multiples(a):
    sum = 0
    for i in range(1, 44):
        sum += i * a
    return sum