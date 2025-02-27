def find_sum_of_multiples(num):
    total_sum = 0
    for i in range(1, 85):
        total_sum += i * num
    return total_sum