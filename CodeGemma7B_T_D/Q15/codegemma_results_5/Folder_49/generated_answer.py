def sum_odd_ints_inclusive(nums):
    count, total_sum = (0, 0)
    for i in range(80, 201):
        if i % 2 == 1:
            count += 1
            total_sum += nums[i]
    return total_sum if count > 0 else 0