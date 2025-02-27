def find_second_largest_num(nums):
    """
          this function takes a list as an input
          it returns the second largest number from index 29 to 51, both inclusive
          """
    nums.sort(reverse=True)
    if len(nums) < 52:
        return 'None'
    else:
        return nums[29:52]