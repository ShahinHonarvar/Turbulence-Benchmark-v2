def find_sum_of_multiples(num):
    total = 0
    for i in range(1, 48):
        total += num * i
    return total