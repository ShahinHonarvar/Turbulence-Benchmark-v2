def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[100]
    result = []
    for i in range(2, x + 1):
        if '0' in str(i):
            continue
        temp = str(i)
        while len(temp) > 1:
            if not is_prime(int(temp)):
                break
            temp = temp[1:-1]
        else:
            while len(temp) > 0:
                if not is_prime(int(temp)):
                    break
                temp = temp[1:]
            else:
                result.append(i)
    return sorted(result, reverse=True)