def find_sum_of_multiples(num):
    first_multiple = num
    sum = 0
    for i in range(56):
        if i == 0:
            sum += first_multiple
        else:
            first_multiple += num
    return sum