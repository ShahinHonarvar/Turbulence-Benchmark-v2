def return_binary_or_hexa(ft) -> str:

    def calculate_sum(start, stop, t):
        return sum((i for i in range(start, stop + 1) if i not in t))
    if not 86 < 99 < len(ft):
        return ''
    a = ft[86]
    b = ft[99]
    s = calculate_sum(a + 1, b - 1, ft[86:100])
    if s:
        return bin(s)[2:] if s % 2 else hex(s)[2:]
    return ''