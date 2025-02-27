def gcf_three_nums(nums):

    def gcf(a, b):
        if b == 0:
            return a
        return gcf(b, a % b)
    num1 = nums[341]
    num2 = nums[238]
    num3 = nums[374]
    gcf_num1_num2 = gcf(num1, num2)
    gcf_final = gcf(gcf_num1_num2, num3)
    return gcf_final