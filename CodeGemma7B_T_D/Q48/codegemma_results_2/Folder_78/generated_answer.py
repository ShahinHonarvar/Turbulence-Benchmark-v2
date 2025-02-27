def return_binary_or_hexa(nums):
    """
  Return binary or hexadecimal representation of the sum of missing values in a sorted tuple,
  if the sum is an odd number, return binary otherwise hexadecimal.
  """
    a, b = (nums[62], nums[96])
    suffix = []
    for i in range(a + 1, b):
        if i not in nums:
            suffix.append(str(i))
    if not suffix:
        return ''
    sum_of_missing_values = sum((int(x) for x in suffix))
    if sum_of_missing_values % 2 == 1:
        return ''.join(suffix)[::-1]
    else:
        return hex(sum_of_missing_values)[2:].upper()