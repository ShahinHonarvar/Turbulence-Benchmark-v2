def gcf_three_nums(nums):
    """
    Greatest common factor of three numbers using Euclid's algorithm.
    """
    x, y, z = (nums[93], nums[94], nums[57])
    while y and z:
        if y > z:
            x, y, z = (y, y % z, z)
        else:
            x, y, z = (x, x % y, y)
    if not y:
        return x
    else:
        return z