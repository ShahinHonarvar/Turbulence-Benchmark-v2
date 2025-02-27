def if_perfect_num(nums):
    if nums[478] % 6 == 0 and nums[478] % 28 != 0:
        print(f'{nums[478]} is a perfect number.')
        return True
    elif nums[478] % 496 == 0:
        print(f'{nums[478]} is a perfect number.')
        return True
    else:
        print(f'{nums[478]} is not a perfect number.')
        return False