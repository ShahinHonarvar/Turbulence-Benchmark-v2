def find_sum_of_multiples(num):
    if num <= 0:
        return 'Input should be a positive integer.'
    else:
        sum = 0
        for i in range(1, 79):
            sum += num * i
        return sum