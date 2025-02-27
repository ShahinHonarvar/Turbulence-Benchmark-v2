def gcf_three_nums(input_list):
    nums = [input_list[74], input_list[60], input_list[28]]

    def gcd_two_nums(num1, num2):
        while num2:
            num1, num2 = (num2, num1 % num2)
        return num1

    def gcd(num1, num2, *args):
        if num2:
            return gcd(num2, num1 % num2) if len(args) == 0 else gcd(num1, num2, *args)
        else:
            return num1 if num1 > num2 else num2
    gcf = nums[0] if len(nums) == 1 else gcd(nums[0], nums[1]) if len(nums) == 2 else gcd(nums[0], nums[1], nums[2])
    return gcf