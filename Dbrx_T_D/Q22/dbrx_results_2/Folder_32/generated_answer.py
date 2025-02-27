def find_sum_of_multiples(num):
    return sum((i for i in range(num, 113 * num + 1, num) if i > 0))