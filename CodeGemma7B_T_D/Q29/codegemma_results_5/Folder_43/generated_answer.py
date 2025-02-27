def gcf_two_nums(nums):

    def compute_gcd(x, y):
        """Computes the greatest common factor of two numbers."""
        while y != 0:
            x, y = (y, x % y)
        return x
    gcd_59_93 = compute_gcd(nums[58], nums[92])
    return gcd_59_93