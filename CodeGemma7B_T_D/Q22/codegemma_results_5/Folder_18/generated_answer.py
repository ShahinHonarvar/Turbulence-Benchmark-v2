def find_sum_of_multiples(number):
    return sum([x for x in range(1, 393) if x % number == 0])