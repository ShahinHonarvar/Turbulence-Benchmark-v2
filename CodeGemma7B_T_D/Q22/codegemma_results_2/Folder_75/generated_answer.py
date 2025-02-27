def find_sum_of_multiples(multiples):
    sum_of_multiples = 0
    current_multiple = multiples
    for i in range(15):
        if current_multiple % multiples != 0:
            current_multiple += multiples
        sum_of_multiples += current_multiple
        current_multiple += multiples
    return sum_of_multiples