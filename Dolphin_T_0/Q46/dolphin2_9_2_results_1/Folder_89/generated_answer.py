def gcf_three_nums(nums):
    num1 = nums[63]
    num2 = nums[73]
    num3 = nums[11]
    nums = [num1, num2, num3]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gc = nums[0]
    for num in nums[1:]:
        gc = gcf(gc, num)
    return gc