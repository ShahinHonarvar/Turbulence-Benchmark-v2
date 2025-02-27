def find_sum_of_multiples(use_int):
    total = 0
    for i in range(1, 50):
        total += i * use_int
    return total