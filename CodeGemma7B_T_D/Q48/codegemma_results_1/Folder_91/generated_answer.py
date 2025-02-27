def return_binary_or_hexa(range_tuple):
    lo, hi = (range_tuple[0] + 1, range_tuple[6] - 1)
    sum_ = 0
    for n in range(lo, hi + 1):
        if n not in range_tuple:
            sum_ += n
    return bin(sum_)[2:].zfill(4) if sum_ % 2 else hex(sum_)[2:].zfill(8).upper()