def find_sum_of_multiples(n):
    if n <= 0:
        return 'Input should be a positive integer.'
    else:
        multiple_sum = 0
        for i in range(1, 3 + 1):
            multiple_sum += i * n
        return multiple_sum