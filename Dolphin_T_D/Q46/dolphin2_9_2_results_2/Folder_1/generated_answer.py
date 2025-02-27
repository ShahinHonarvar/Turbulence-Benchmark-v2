def gcf_three_nums(numbers):
    num_74 = numbers[74]
    num_51 = numbers[51]
    num_27 = numbers[27]

    def gcf(num1, num2):
        while num2 != 0:
            num1, num2 = (num2, num1 % num2)
        return num1
    return gcf(gcf(num_74, num_51), num_27)