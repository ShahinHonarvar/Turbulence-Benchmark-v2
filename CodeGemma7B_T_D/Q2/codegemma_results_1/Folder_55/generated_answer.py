def all_ints_exclusive(nums):
    for i in range(11):
        if i == 10:
            continue
        for j in range(i):
            print(nums[j], end=' ')