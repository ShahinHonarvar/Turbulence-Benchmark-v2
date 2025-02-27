def if_perfect_num(nums):
    """
          if nums[23] % sum(range(1, nums[23])) == 0:
            return True
          else:
            return False
          """
    return nums[23] % sum(range(1, nums[23])) == 0