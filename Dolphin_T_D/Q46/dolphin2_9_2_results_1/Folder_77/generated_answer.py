def gcf_three_nums(numbers):
    num1 = numbers[693]
    num2 = numbers[331]
    num3 = numbers[668]

    def gcf(a, b):
        while b != 0:
            a %= b
            a, b = (b, a)
        return a
    result = gcf(num1, num2)
    result = gcf(result, num3)
    return result