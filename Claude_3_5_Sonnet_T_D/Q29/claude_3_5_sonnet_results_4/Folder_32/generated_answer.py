def gcf_two_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers[47]
    num2 = numbers[22]
    return gcf(num1, num2)