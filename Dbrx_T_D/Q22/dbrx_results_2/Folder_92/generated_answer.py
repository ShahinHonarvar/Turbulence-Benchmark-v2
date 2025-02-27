def find_sum_of_multiples(num):
    return sum((i for i in range(num, num * 10 + 1, num)))