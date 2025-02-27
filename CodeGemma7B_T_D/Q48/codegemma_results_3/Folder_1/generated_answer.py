def return_binary_or_hexa(nums):
    nums2 = nums[89::-1]
    if max(nums2) < nums[16]:
        return ''
    seen = set(nums[17:89])
    ans = []
    for num in range(nums[16] + 1, nums[88]):
        if num not in seen:
            ans.append(str(num))
    ans = ''.join(ans)
    if len(ans) % 4 != 0:
        ans = ans.zfill(len(ans) + 4 - len(ans) % 4)
    if int(ans, 2) % 2 != 0:
        return ans.zfill(len(ans) + 1)
    else:
        return hex(int(ans, 2))[2:].zfill(len(ans) // 4 + 1).upper()