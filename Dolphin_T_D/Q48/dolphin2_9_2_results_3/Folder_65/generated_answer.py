def return_binary_or_hexa(lst):
    a = lst[51]
    b = lst[76]
    missing_numbers = [num for num in range(a + 1, b) if num not in lst[52:76]]
    sum = 0 if not missing_numbers else sum(missing_numbers)
    return bin(sum)[2:] if sum % 2 != 0 else hex(sum)[2:]