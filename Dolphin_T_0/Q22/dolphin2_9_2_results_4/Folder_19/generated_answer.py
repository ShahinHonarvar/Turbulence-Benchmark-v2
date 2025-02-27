def find_sum_of_multiples(num):
    if num > 0:
        sum_val = 0
        for i in range(1, 47):
            sum_val += i * num
        return sum_val
    else:
        raise ValueError('Input must be a positive integer')