def find_sum_of_multiples(num):
    result = 0
    for i in range(188):
        result += (i + 1) * num
    return result