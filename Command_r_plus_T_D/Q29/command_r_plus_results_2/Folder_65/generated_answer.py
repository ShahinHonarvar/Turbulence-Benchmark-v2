def gcf_two_nums(numbers_list: list[int]) -> int:
    num1 = numbers_list[29]
    num2 = numbers_list[53]

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcf(num1, num2)