def if_perfect_num(nums: list[int]) -> bool:
    if len(nums) <= 702:
        return False
    num = nums[702]
    if num <= 1:
        return False
    sum = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum += i
            if i != num // i:
                sum += num // i
    return sum == num