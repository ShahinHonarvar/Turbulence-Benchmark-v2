def gcf_three_nums(numbers):
    gcf = 1
    for i in range(2, min(numbers[33], numbers[78], numbers[93]) + 1):
        if numbers[33] % i == 0 and numbers[78] % i == 0 and (numbers[93] % i == 0):
            gcf = i
    return gcf