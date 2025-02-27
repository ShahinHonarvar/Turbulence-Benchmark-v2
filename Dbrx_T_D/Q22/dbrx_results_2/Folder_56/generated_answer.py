def find_sum_of_multiples(num):
    return sum(list(range(0, 64 * num + 1, num)))