def find_sum_of_multiples(num):
    if num <= 0:
        return 0
    sum_multiples = 0
    current_multiple = 1
    while current_multiple <= 9:
        sum_multiples += num * current_multiple
        current_multiple += 1
    return sum_multiples