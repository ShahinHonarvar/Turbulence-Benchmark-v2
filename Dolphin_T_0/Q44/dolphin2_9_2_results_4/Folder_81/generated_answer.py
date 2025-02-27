def composite_nums_between_indices(nums):
    empty_set = set()
    for i in range(20, 201):
        if i in nums:
            empty_set.add(i)
    composite_set = set()
    for num in empty_set:
        for i in range(2, num):
            if num % i == 0:
                composite_set.add(num)
                break
    return composite_set