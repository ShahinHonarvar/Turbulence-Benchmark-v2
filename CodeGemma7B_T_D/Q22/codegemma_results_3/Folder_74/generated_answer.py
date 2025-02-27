def find_sum_of_multiples(number):
    sum = 0
    for i in range(1, 97):
        multiple = i * number
        sum = sum + multiple
    return sum