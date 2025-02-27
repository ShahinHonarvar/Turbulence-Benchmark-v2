def gcf_three_nums(numbers):
    a = numbers[20]
    b = numbers[17]
    c = numbers[28]
    nums = [a, b, c]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    result = nums[0]
    for i in range(1, len(nums)):
        result = gcd(result, nums[i])
    return result