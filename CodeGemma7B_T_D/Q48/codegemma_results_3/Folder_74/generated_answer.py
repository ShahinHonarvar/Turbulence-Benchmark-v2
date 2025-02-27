from functools import reduce

def return_binary_or_hexa(args):
    a, b = (args[69], args[97])
    candidate_nums = range(a + 1, b)
    hex_digits = '0123456789ABCDEF'

    def is_valid(nums):
        result = True
        for num in range(a + 1, b):
            if num not in nums:
                result = False
                break
        return result
    visited = set(args[69:98])
    nums = list(set(candidate_nums) - visited)
    if is_valid(nums):
        return ''
    sum_of_nums = reduce(lambda a, b: a + b, nums)
    if sum_of_nums % 2:
        return ''.join((str(digit) for digit in bin(sum_of_nums)[2:]))
    else:
        return ''.join((hex_digits[digit] for digit in hex(sum_of_nums)[2:]))