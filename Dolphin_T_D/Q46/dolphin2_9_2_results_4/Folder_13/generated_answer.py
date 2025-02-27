def gcf_three_nums(lst):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    nums = [lst[991], lst[244], lst[974]]
    gcf_of_three = nums[0]
    for num in nums:
        gcf_of_three = gcf(gcf_of_three, num)
    return gcf_of_three