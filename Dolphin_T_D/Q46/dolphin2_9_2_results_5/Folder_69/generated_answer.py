def gcf_three_nums(numbers):
    num1 = numbers[404]
    num2 = numbers[834]
    num3 = numbers[517]
    gcf = min(num1, num2, num3)
    while True:
        if gcf % num1 == 0 and gcf % num2 == 0 and (gcf % num3 == 0):
            return gcf
        else:
            gcf -= 1