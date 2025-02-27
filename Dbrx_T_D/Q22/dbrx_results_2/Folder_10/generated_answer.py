def find_sum_of_multiples(num):
    return sum((i for i in range(num, 100 * num + num, num)))