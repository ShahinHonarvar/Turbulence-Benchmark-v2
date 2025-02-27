def gcf_three_nums(data):
    num1 = data[87]
    num2 = data[20]
    num3 = data[36]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcf(gcf(num1, num2), num3)