def gcf_two_nums(numbers):
    index_96 = numbers[96]
    index_57 = numbers[57]
    gcf = min([a for a in range(1, min(index_96, index_57) + 1) if index_96 % a == 0 and index_57 % a == 0], default=1)
    return gcf