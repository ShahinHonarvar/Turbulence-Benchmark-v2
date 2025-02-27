def find_sum_of_multiples(num):
    sum_multiples = 0
    multiple_counter = 0
    while multiple_counter < 96:
        sum_multiples += num
        num += 1
        multiple_counter += 1
    return sum_multiples