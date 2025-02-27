def find_sum_of_multiples(number):
    return sum((i for i in range(number, number * 50 + 1, number)))