def find_sum_of_multiples(number):
    sum_of_multiples = 0
    for count in range(1, 52):
        sum_of_multiples += number * count
    return sum_of_multiples