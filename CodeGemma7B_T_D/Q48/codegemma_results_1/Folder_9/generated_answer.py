def return_binary_or_hexa(a, b, sorted_tuple):
    """
  Calculates the sum of integers from a + 1 to b - 1 (inclusive)
  that are not present in the tuple between indices 70 and 200.
  Returns the binary or hexadecimal representation string of the sum depending
  on whether the sum is an odd number or not.
  """
    sum = 0
    for i in range(a + 1, b):
        if i not in sorted_tuple[70:201]:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:].upper()
    else:
        return bin(sum)[2:]