def find_sum_of_multiples(number):
    if number < 1:
        return 0
    sum = 0
    for i in range(1, 256):
        sum += i * number
    return sum