def if_decimal_is_divisible(binary_str):

    def bin_to_dec(binary_str):
        decimal_num = 0
        for digit in binary_str:
            decimal_num = (decimal_num << 1) + int(digit)
        return decimal_num
    golden_ratio_plus_one = (1 + 5 ** 0.5) / 2
    seventh_fibonacci = round(golden_ratio_plus_one ** 6)
    return bin_to_dec(binary_str) % seventh_fibonacci == 0