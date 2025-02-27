def composite_nums_between_indices(nums):
    result = set()
    for num in nums:
        if 111 <= nums.index(num) <= 111:
            composite = False
            if num > 1:
                for i in range(2, num):
                    if num % i == 0:
                        composite = True
                        break
            if composite:
                result.add(num)
    return result