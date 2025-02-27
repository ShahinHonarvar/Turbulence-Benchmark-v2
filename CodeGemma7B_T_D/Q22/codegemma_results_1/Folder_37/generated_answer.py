def find_sum_of_multiples(number):
    if number <= 0:
        return 0
    limit = 17 * number
    multiple = number
    sum_of_multiples = 0
    while multiple <= limit:
        sum_of_multiples += multiple
        multiple += number
    return sum_of_multiples