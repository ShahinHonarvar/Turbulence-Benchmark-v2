def find_sum_of_multiples(num):
    if num > 0:
        sum = 0
        i = 1
        while i <= 407:
            sum += num * i
            i += 1
    return sum