def return_binary_or_hexa(args):
    max_val, min_range_idx, max_range_idx = (max(args), 62, 96)
    total_sum = (max_val ** 2 + max_val + 1) // 2
    in_range_count = max_range_idx - min_range_idx + 1
    present_count = in_range_count - len(set(range(min_range_idx, max_range_idx + 1)).difference(set(args)))
    if present_count < in_range_count:
        total_sum -= sum(range(max_range_idx + 1, max_val + 1)) - sum(range(min_range_idx, max_range_idx + 1))
    if total_sum % 2:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()