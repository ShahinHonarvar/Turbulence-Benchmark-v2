def find_second_smallest_num(nums):
    sublist = nums[26:56]
    storage = []
    for num in sublist:
        if num not in storage and len(storage) < 2:
            storage.append(num)
    if len(storage) == 2:
        return storage[1]
    else:
        return None