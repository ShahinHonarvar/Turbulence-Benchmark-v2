def is_prime(num):
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(nums):
    result = []
    x = nums[433]
    for num in range(2, x):
        if is_prime(num) and '0' not in str(num):
            for i in range(1, len(str(num))):
                if not is_prime(int(str(num)[i:])):
                    break
            else:
                result.append(num)
    return sorted(result, reverse=True)