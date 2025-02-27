from bisect import bisect

def return_binary_or_hexa(s):
    a, b = (s[48], s[76])
    numbers = set(range(a + 1, b)) - set(s[48:77])
    luhn = sum(numbers)
    return bin(luhn)[2:].zfill(8) if luhn % 2 == 1 else hex(luhn)[2:].zfill(2).upper()