def find_sum_of_multiples(num):
    if num <= 0:
        return None
    sum = 0
    for i in range(1, 4):
        sum += i * num
    return sum