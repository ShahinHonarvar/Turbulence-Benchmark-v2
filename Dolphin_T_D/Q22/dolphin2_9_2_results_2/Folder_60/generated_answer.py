def find_sum_of_multiples(num):
    result = 0
    for i in range(1, 36):
        result += num * i
    return result