def gcf_three_nums(nums):
    n1 = nums[76]
    n2 = nums[64]
    n3 = nums[28]

    def gcf(n1, n2, n3):
        if n1 == 0 and n2 == 0 and (n3 == 0):
            return 0
        else:
            for i in range(1, min(n1, n2, n3) + 1):
                if n1 % i == 0 and n2 % i == 0 and (n3 % i == 0):
                    gcf = i
            return gcf
    return gcf(n1, n2, n3)