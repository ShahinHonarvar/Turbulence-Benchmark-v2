def find_sum_of_multiples(given_number):
    sum_of_multiples = 0
    for number in range(1, 35):
        sum_of_multiples += number * given_number
    return sum_of_multiples