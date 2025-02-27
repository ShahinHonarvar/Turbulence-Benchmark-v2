def gcf_two_nums(nums_list):
    num1 = nums_list[90]
    num2 = nums_list[84]

    def gcf(a, b):
        if a % b == 0:
            return b
        return gcf(b, a % b)
    return gcf(num1, num2)