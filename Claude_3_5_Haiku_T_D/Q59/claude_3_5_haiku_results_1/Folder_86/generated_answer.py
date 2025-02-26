def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[126]
    result = []
    for n in range(x - 1, 1, -1):
        s = str(n)
        if '0' in s:
            continue
        truncatable = True
        for i in range(len(s)):
            trunc_num = int(s[i:])
            if not is_prime(trunc_num):
                truncatable = False
                break
        if truncatable and is_prime(n):
            result.append(n)
    return result