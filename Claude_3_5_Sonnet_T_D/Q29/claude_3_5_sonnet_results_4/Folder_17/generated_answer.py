def gcf_two_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers[69]
    num2 = numbers[40]
    return gcf(num1, num2)