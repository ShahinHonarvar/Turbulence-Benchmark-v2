def gcf_two_nums(nums):
    num1 = nums[871]
    num2 = nums[218]
    greater = max(num1, num2)
    smaller = min(num1, num2)
    while smaller != 0:
        remain = greater % smaller
        greater = smaller
        smaller = remain
    return greater