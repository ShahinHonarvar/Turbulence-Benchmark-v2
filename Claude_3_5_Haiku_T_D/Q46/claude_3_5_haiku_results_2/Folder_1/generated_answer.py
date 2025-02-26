def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    n1 = nums[74]
    n2 = nums[51]
    n3 = nums[27]
    first_gcf = gcd(n1, n2)
    final_gcf = gcd(first_gcf, n3)
    return final_gcf