def find_sum_of_multiples(number):
    multiples = [x for x in range(1, 28 * number + 1) if x % number == 0]
    return sum(multiples)