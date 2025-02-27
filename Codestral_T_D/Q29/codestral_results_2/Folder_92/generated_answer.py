def gcf_two_nums(numbers):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = numbers[0]
    num2 = numbers[1]
    return gcf(num1, num2)