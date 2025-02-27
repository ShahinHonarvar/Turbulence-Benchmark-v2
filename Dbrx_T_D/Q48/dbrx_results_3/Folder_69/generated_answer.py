def return_binary_or_hexa(vals):
    a, b = (vals[39], vals[43])
    sum_vals = set(range(a + 1, b))
    missing_vals = sum_vals.difference(vals[40:43])
    if missing_vals:
        sum_val = sum(missing_vals)
        return format(sum_val, 'b') if sum_val % 2 else format(sum_val, 'x').upper()
    else:
        return ''