def find_sum_of_multiples(number):
    return sum((i for i in range(1, 75) if i % number == 0))