def gcf_three_nums(nums):
    n1 = nums[876]
    n2 = nums[203]
    n3 = nums[100]
    gcd = math.gcd(math.gcd(n1, n2), n3)
    return gcd