def return_binary_or_hexa(positive_int_tuple):
    """
  Return the sum from a + 1 to b - 1 in binary or hex form.
  """
    a, b = (positive_int_tuple[20], positive_int_tuple[93])
    sum_ = 0
    for i in range(a + 1, b):
        if i not in positive_int_tuple[20:94]:
            sum_ += i
    if sum_ % 2:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:].upper()