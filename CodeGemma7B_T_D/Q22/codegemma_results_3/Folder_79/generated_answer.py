def find_sum_of_multiples(num):
    sum = 0
    i = 0
    while i <= 27:
        if i == 0:
            i = num
        else:
            i += num
        sum = sum + i
    return sum