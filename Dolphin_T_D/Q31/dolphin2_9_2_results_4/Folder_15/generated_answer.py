def if_perfect_num(nums):
    if len(nums) < 11:
        return False
    else:
        num = nums[10]
        divs = [1]
        for i in range(2, num):
            if num % i == 0:
                divs.append(i)
        return sum(divs) == num