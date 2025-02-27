def if_perfect_num(nums):
    num = nums[222]
    if num > 1:
        i = 2
        while i * i <= num:
            if num % i == 0 and num / i != i:
                return False
            for j in range(2, int(num / i)):
                if num % i == 0 and num / i == j:
                    return False
            i += 1
    return True