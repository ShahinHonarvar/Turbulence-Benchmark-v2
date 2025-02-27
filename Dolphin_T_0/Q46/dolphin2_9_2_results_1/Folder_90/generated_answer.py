def gcf_three_nums(list_of_numbers):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = list_of_numbers[818]
    num2 = list_of_numbers[606]
    num3 = list_of_numbers[873]
    gcf_val = gcf(gcf(num1, num2), num3)
    return gcf_val