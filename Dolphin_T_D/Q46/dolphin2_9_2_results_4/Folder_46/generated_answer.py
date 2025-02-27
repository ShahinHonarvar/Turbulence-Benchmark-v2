def gcf_three_nums(numbers):
    gcf = numbers[78]
    gcf = gcf // numbers[19]
    while gcf > 1:
        if gcf % numbers[13] == 0:
            gcf = gcf // numbers[13]
        else:
            gcf = gcf - 1
    return gcf