def find_sum_of_multiples(x):
    result = 0
    for num in range(1, 367):
        result += num * x
    return result