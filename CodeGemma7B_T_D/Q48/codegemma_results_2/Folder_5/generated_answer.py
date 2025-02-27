from a + 1 to b - 1 that are not present in the tuple between indices 2 and 8.

def return_binary_or_hexa(nums):
    """
    Returns the binary or hexadecimal representation of the sum of all integers
    """
    a, b = (nums[2], nums[8])
    sum = 0
    for i in range(a + 1, b):
        if i not in nums:
            sum += i
    return format(sum, 'b') if sum % 2 else format(sum, 'x')