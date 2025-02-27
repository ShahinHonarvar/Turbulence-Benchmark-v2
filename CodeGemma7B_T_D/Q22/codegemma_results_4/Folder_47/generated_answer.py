def find_sum_of_multiples(num):
    sum_of_multiples = 0
    current_multiple = 1
    while current_multiple <= 38:
        sum_of_multiples += current_multiple * num
        current_multiple += 1
    return sum_of_multiples