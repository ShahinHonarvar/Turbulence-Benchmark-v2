def find_sum_of_multiples(num):
    result = 0
    for i in range(1, 420):
        if i % num == 0:
            result += i
    return result