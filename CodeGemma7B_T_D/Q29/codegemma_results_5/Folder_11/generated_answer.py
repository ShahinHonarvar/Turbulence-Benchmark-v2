def gcf_two_nums(nums):
    num_sixty_four = nums[64]
    num_eighty = nums[80]
    while num_sixty_four % num_eighty != 0:
        num_temp = num_sixty_four % num_eighty
        num_sixty_four = num_eighty
        num_eighty = num_temp
    return num_eighty