from a to b where a is at index 20 and b is at index 51, and all numbers in the range (a + 1, b)

def return_binary_or_hexa(nums):
    """
            This function takes one argument, a tuple of distinct nonnegative integers sorted in ascending order
            and returns the binary or hexadecimal representation of the sum of all numbers in the range (a + 1, b)
            are not present in the tuple. It removes the zeros from each number (b/w a+1 and b) if any exist
            and then sums them up. If the sum is an odd number, it returns the binary representation of the sum and 
            if it's an even number, it returns the hexadecimal representation.
            """
    a = nums[20]
    b = nums[51]
    sum = 0
    for num in nums[21:51]:
        if num not in nums[20:51]:
            sum += num
    if sum % 2 == 0:
        return '%x' % sum
    else:
        return bin(sum)[2:]