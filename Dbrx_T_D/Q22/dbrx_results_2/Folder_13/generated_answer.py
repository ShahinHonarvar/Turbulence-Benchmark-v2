def find_sum_of_multiples(num):
    return sum((i for i in range(num, 206 * num + num, num)))