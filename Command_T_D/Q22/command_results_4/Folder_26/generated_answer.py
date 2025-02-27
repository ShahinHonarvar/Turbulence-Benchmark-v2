def find_sum_of_multiples(n):
    sum_of_multiples = 0
    multiple = 1
    max_multiple = n * 366
    for i in range(1, max_multiple + 1):
        if i % n == 0:
            sum_of_multiples += i
        multiple = i
    return sum_of_multiples