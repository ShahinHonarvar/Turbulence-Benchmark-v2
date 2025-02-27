def all_right_truncatable_prime(nums):
    x = nums[618]
    prime = [2, 3, 5, 7]
    ans = []
    size = len(str(x))
    remove_num = 2
    for d in range(2, x):
        if len(str(d)) > size:
            continue
        flag = 1
        num = d
        for s in range(len(str(d)) - 1):
            num = int(str(num)[:-1])
            if str(num) not in prime:
                flag = 0
                break
        if flag == 1:
            ans.append(d)
        remove_num += 1
    ans.sort()
    return ans