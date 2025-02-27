def gcf_three_nums(nums):
    a = nums[16]
    b = nums[87]
    c = nums[95]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf = gcd(a, b)
    gcf = gcd(gcf, c)
    return gcf