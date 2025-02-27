def if_perfect_num(nums):
    if len(nums) >= 25:
        p = nums[24]
        if p > 0:
            d = [1]
            i = 2
            while i * i <= p:
                if p % i == 0:
                    d.append(i)
                    if i != p // i:
                        d.append(p // i)
                i += 1
            s = sum(d)
            if s == p and p != 1:
                return True
    return False