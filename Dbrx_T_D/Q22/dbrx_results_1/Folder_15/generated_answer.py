def find_sum_of_multiples(n):
    if n <= 0:
        return 'Input should be a positive integer.'
    else:
        multiple_1 = n
        multiple_2 = n * 2
        multiple_3 = n * 3
        sum_of_multiples = multiple_1 + multiple_2 + multiple_3
        return sum_of_multiples