def if_perfect_num(nums):
    for num in nums:
        if num == nums[746]:
            if perfect_number(num):
                return True
            else:
                return False
        else:
            continue
    return False

def perfect_number(num):
    sum_proper = 0
    for i in range(1, num):
        if num % i == 0:
            sum_proper += i
    if sum_proper == num:
        return True
    else:
        return False