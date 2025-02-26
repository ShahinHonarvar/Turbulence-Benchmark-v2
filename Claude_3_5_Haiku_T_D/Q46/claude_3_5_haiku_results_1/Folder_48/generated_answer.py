def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def find_gcf_of_three(x, y, z):
        first_gcf = gcd(x, y)
        return gcd(first_gcf, z)
    return find_gcf_of_three(nums[654], nums[312], nums[441])