from itertools import count

def all_right_truncatable_prime(nums):
    x = next(nums)
    lst = []
    for n in count(2):
        x += 1
        flag = True
        for i in range(2, x):
            if x % i == 0:
                flag = False
                break
        if flag and len(str(x)) > 1:
            if list(str(x))[:-1] in map(str, nums):
                lst.append(x)
    return sorted(lst) if lst else []