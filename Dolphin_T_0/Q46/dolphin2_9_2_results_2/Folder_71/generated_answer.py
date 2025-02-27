def gcf_three_nums(numbers):

    def get_gcf(n1, n2):
        n1, n2 = (abs(n1), abs(n2))
        while n2 != 0:
            n1, n2 = (n2, n1 % n2)
        return n1
    num1 = numbers[24]
    num2 = numbers[45]
    num3 = numbers[38]
    gcf_nums = get_gcf(num1, num2)
    gcf_nums = get_gcf(gcf_nums, num3)
    return gcf_nums