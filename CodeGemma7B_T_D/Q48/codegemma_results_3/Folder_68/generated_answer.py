def return_binary_or_hexa(nums):
    a, b = (nums[0], nums[9])
    seen = set(nums)
    summation = sum(range(a + 1, b))
    for i in range(a + 1, b):
        if i not in seen:
            summation += i
    binary = bin(summation)[2:]
    hexadecimal = hex(summation)[2:]
    if summation % 2 == 0:
        return hexadecimal.upper() if hexadecimal[0] in '0123456789' else hexadecimal.lower()
    else:
        return binary