def find_sum_of_multiples(number):
    multiples = [number * i for i in range(1, 24)]
    return sum(multiples)