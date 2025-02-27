def find_sum_of_multiples(number):
    res = 0
    for i in range(1, 85):
        res += i * number
    return res