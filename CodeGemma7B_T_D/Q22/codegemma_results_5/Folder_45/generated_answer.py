def find_sum_of_multiples(number):
    return sum(range(number, (number + 36) * number + 1, number))