def composite_nums_between_indices(nums):
    """
  This function takes a list of positive integers and returns the set of all composite numbers in the given list between index 17 to index 78, both inclusive. If no composite number exists in the specified range, the function returns an empty set.
  """
    composite_nums = set()
    for num in nums[17:78 + 1]:
        for i in range(2, num):
            if num % i == 0:
                composite_nums.add(num)
                break
    return composite_nums