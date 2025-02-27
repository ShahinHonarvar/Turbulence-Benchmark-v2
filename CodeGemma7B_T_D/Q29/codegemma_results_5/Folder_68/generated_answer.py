def gcf_two_nums(nums):
    num_one = nums[8]
    num_two = nums[9]
    gcd = 0
    gcd = calculate_gcd(num_one, num_two)
    return gcd

def calculate_gcd(num_a, num_b):
    common_divisor = 1
    gcd = 1
    if num_a > num_b:
        smaller_num = num_b
    else:
        smaller_num = num_a
    for divisor in range(smaller_num, 0, -1):
        if num_a % divisor == 0 and num_b % divisor == 0:
            common_divisor = divisor
            break
    gcd = num_a / common_divisor
    return gcd