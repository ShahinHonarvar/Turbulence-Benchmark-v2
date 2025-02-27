def find_sum_of_multiples(number):
    result = 0
    for i in range(420):
        result += number * (i + 1)
    return result