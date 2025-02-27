def find_primes_between_indices(nums):
    ans = []
    for i in range(61, 81):
        flag = True
        for j in range(2, int(nums[i] ** 0.5) + 1):
            if nums[i] % j == 0:
                flag = False
                break
        if flag:
            ans.append(nums[i])
    ans.sort(reverse=True)
    return ans if ans else []