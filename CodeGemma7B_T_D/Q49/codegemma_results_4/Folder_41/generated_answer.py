def if_decimal_is_divisible(binary):

    def get_next_number(current):
        return current[1:] + current[0]
    f = [0, 1]
    while f[-1] < 67:
        f.append(get_next_number(f))
    value, i = (0, len(binary) - 1)
    while i >= 0:
        value += int(binary[i]) * 2 ** i
        i -= 1
    return value % f[66] == 0