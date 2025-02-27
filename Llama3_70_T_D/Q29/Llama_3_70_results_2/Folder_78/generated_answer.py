def gcf_two_nums(nums):

    def calculate_gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = nums[54]
    num2 = nums[13]
    return calculate_gcf(num1, num2)