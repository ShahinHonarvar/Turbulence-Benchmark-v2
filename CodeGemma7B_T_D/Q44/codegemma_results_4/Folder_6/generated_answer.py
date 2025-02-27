from math import sqrt

def composite_nums_between_indices(nums):
    prime_nos = [True] * (max(nums) + 1)
    for i in range(2, int(sqrt(max(nums))) + 1):
        if prime_nos[i]:
            for j in range(i * i, max(nums) + 1, i):
                prime_nos[j] = False
    composites = set()
    for i in range(13, 68):
        if (i >= 0 and i < len(nums)) and (not prime_nos[nums[i]]):
            composites.add(nums[i])
    returncomposites