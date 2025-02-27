def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[88]
    result = []
    for num in range(10, x + 1):
        if '0' not in str(num) and is_prime(num):
            num_str = str(num)
            left_truncatable = all((is_prime(int(num_str[i:])) for i in range(1, len(num_str))))
            right_truncatable = all((is_prime(int(num_str[:len(num_str) - i])) for i in range(1, len(num_str))))
            if left_truncatable and right_truncatable:
                result.append(num)
    return sorted(result, reverse=True)