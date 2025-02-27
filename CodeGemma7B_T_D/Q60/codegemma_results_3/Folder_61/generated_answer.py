def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def truncate(num):
    trunc = []
    for i in range(len(str(num))):
        trunc.append(int(str(num)[i:]))
        trunc.append(int(str(num)[:-i - 1]))
    return trunc

def all_left_right_truncatable_prime(nums):
    x = nums[3]
    result = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        if is_prime(num):
            temp = truncate(num)
            temp = list(set(temp))
            if all((is_prime(n) for n in temp)):
                result.append(num)
    if len(result) == 0:
        return []
    return sorted(result, reverse=True)