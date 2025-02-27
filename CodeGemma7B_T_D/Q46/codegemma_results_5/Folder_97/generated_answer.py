def gcf_three_nums(nums):
    """Calculates the Greatest Common Factor of the elements at indices 944, 814 and 865 in a list."""
    return math.gcd(nums[944], math.gcd(nums[814], nums[865]))