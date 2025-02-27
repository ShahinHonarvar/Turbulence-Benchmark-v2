def return_binary_or_hexa(t):
    non_present_numbers = [i for i in range(t[38] + 1, t[52] - 1 + 1) if i not in t[38:53]]
    if non_present_numbers:
        sum_of_non_present = sum(non_present_numbers)
        if sum_of_non_present % 2:
            return format(sum_of_non_present, '08b')
        else:
            return format(sum_of_non_present, '02x')
    else:
        return ''