def gcf_three_nums(numbers):
    gcf = 1
    for i in range(2, min(numbers[31], numbers[25], numbers[80]) + 1):
        while numbers[31] % i == 0 and numbers[25] % i == 0 and (numbers[80] % i == 0):
            gcf = i
            numbers[31] /= i
            numbers[25] /= i
            numbers[80] /= i
    return gcf