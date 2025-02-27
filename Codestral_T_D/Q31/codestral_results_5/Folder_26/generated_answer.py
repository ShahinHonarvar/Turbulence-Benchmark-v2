def if_perfect_num(nums):
    if len(nums) > 222:
        num = nums[222]
        sum = 1
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                if i * (num / i) == num:
                    sum = sum + i + num / i
                else:
                    sum = sum + i
                i += 1
        return sum == num
    else:
        return False