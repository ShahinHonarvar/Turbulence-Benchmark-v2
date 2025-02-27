def gcf_two_nums(numbers_list):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers_list[84]
    num2 = numbers_list[13]
    return gcf(num1, num2)