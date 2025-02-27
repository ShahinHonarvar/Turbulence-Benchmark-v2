def find_sum_of_multiples(number):
    sum_of_multiples = 0
    for i in range(64):
        multiple = i * number
        if multiple <= 63:
            sum_of_multiples += multiple
    return sum_of_multiples