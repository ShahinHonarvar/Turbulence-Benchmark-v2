def find_sum_of_multiples(n):
    sum = 0
    current_multiple = n
    for _ in range(56):
        sum += current_multiple
        current_multiple += n
    return sum