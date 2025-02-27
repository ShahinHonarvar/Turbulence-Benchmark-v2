from a + 1 to b - 1 (both inclusive) that are not present in the tuple.

def return_binary_or_hexa(*nums):
    """ 
  Given a tuple of distinct nonnegative integers sorted in ascending order, 
  returns the binary or hexadecimal representation of the sum of all integers 
  """
    nums = list(nums)
    a, b = (nums[13], nums[76])
    more, result, unbound = (0, [], b + 1)
    while a < unbound:
        if nums[more] == a:
            a += 1
            more += 1
        elif nums[more] > a:
            result.append(a)
            a += 1
        else:
            more += 1
    if result:
        if sum(result) % 2 == 0:
            return ''.join(result).zfill(2).upper()
        else:
            return ''.join(map('{0:b}'.format, result)).strip('0')
    else:
        return ''