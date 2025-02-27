def find_sum_of_multiples(num):
    sum = 0
    for i in range(num, 318 * num + 1, num):
        sum += i
    return sum