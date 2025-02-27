def if_perfect_num(nums):
    if nums[247] > 0:
        sum = 1
        end = int(nums[247] ** 0.5)
        for i in range(2, end + 1):
            if nums[247] % i == 0:
                if i * i != nums[247]:
                    sum = sum + i + nums[247] // i
                else:
                    sum = sum + i
        if sum == nums[247]:
            return True
    return False