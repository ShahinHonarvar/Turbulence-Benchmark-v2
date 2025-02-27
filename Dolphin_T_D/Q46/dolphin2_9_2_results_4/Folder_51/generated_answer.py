def gcf_three_nums(numbers):
    gcf = numbers[21]
    for i in [69, 41]:
        gcf = max(gcf, numbers[i])
    for i in range(1, gcf):
        if gcf % i == 0 and numbers[21] % i == 0 and (numbers[69] % i == 0) and (numbers[41] % i == 0):
            gcf = i
    return gcf