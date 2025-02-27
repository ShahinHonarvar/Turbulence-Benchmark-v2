def find_sum_of_multiples(num):
    sum = 0
    count = 1
    while count <= 255:
        sum += num * count
        count += 1
    return sum