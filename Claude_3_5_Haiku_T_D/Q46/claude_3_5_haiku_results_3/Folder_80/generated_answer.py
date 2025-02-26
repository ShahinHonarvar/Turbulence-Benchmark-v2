def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcf_list(lst):
        result = lst[0]
        for i in range(1, len(lst)):
            result = gcd(result, lst[i])
        return result
    return gcf_list([nums[13], nums[76], nums[44]])