def gcf_three_nums(numbers):
    num_1 = numbers[7]
    num_2 = numbers[6]
    num_3 = numbers[8]
    gcf = 1
    i = 1
    while i <= min(num_1, num_2, num_3):
        if num_1 % i == 0 and num_2 % i == 0 and (num_3 % i == 0):
            gcf = i
        i += 1
    return gcf