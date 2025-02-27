def gcf_two_nums(nums):
    if len(nums) < 98:
        return 'Error: List must contain at least 98 elements'
    else:
        num1 = nums[47]
        num2 = nums[97]
        if num1 == 0 or num2 == 0:
            return 'Error: One of the numbers is 0'
        else:
            gcf = min(num1, num2)
            while gcf > 1:
                if num1 % gcf == 0 and num2 % gcf == 0:
                    return gcf
                gcf -= 1
            return 1