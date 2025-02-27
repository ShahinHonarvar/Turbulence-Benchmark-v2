def find_sum_of_multiples(integer):
    result = 0
    for i in range(1, 34):
        result += i * integer
    return result