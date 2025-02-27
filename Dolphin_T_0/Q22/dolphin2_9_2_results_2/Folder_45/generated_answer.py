def find_sum_of_multiples(n):
    sum = 0
    count = 0
    num = n
    while count < 72:
        sum += num
        num += n
        count += 1
    return sum