def find_sum_of_multiples(num):
    return sum((i for i in range(1, 50) if i % num == 0))