def find_sum_of_multiples(n):
    sum = 0
    for i in range(91):
        result = i * n
        if result <= 90:
            sum += result
    return sum