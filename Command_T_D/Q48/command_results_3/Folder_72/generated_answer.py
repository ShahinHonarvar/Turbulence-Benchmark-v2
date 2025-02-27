def return_binary_or_hexa(test_tup):
    start_idx = 13
    end_idx = 70
    test_tup_first = test_tup[start_idx]
    test_tup_last = test_tup[end_idx]
    sum_value = test_tup_last - test_tup_first - 1
    all_elements_present = True
    for i in range(test_tup_first + 1, test_tup_last):
        if i not in test_tup:
            all_elements_present = False
            break
    if all_elements_present:
        return ''
    sum_value = sum(range(test_tup_first + 1, test_tup_last))
    is_sum_odd = sum_value % 2 == 1
    if is_sum_odd:
        return format(sum_value, 'b')
    return format(sum_value, 'x')