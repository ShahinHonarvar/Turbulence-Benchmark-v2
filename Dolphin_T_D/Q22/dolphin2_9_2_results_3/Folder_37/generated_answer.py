def find_sum_of_multiples(n):
    if n < 0:
        return 'Invalid input: n must be a positive integer.'
    else:
        sum = 0
        for i in range(1, 18):
            sum += i * n
        return sum