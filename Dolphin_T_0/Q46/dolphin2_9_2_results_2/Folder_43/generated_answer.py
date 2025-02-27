def gcf_three_nums(numbers):
    num1 = numbers[33]
    num2 = numbers[78]
    num3 = numbers[93]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf_num = gcf(num1, num2)
    gcf_all = gcf(gcf_num, num3)
    return gcf_all