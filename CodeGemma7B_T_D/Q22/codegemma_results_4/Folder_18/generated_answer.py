def find_sum_of_multiples(n):
    sum_of_multiples = 0
    for num in range(1, 393):
        multiple = n * num
        sum_of_multiples += multiple
    return sum_of_multiples