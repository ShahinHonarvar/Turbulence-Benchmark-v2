def find_sum_of_multiples(num):
    result = 0
    for i in range(1, 42):
        result += i * num
    return result