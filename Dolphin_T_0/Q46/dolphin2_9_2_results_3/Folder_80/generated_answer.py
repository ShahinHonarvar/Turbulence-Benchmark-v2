def gcf_three_nums(arr):
    num1 = arr[13]
    num2 = arr[76]
    num3 = arr[44]

    def gcf(a, b):
        while b > 0:
            a, b = (b, a % b)
        return a
    return gcf(gcf(num1, num2), num3)