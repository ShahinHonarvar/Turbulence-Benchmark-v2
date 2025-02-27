def if_perfect_num(nums):
    sum_facts = 0
    for num in range(1, nums[0]):
        if nums[0] % num == 0:
            sum_facts += num
    if sum_facts == nums[0]:
        return True
    else:
        return False