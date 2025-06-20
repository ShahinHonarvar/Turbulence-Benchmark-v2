def gcf_two_nums(numbers_list):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers_list[380]
    num2 = numbers_list[327]
    return gcf(num1, num2)