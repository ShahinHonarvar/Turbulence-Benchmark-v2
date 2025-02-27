def find_sum_of_multiples(num):
    if num <= 0:
        return 'Input should be a positive integer'
    return sum((i * num for i in range(1, 92)))