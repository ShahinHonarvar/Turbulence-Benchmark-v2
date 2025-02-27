def return_binary_or_hexa(lst):
    a, b = (lst[10], lst[79])
    missing_nums = [i for i in range(a + 1, b) if i not in lst[10:80]]
    if not missing_nums:
        return ''
    total = sum(missing_nums)
    if total % 2 == 0:
        return '{0:x}'.format(total)
    else:
        return bin(total)[2:]