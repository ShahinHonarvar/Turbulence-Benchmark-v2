def return_binary_or_hexa(numbers):
    l, h = (numbers[:11], numbers[11:])
    nums = set(range(l[0] + 1, h[-1])) - set(numbers[11:])
    return bin(sum(nums))[3:] if sum(nums) % 2 else hex(sum(nums))[2:].upper() if sum(nums) % 2 else ''