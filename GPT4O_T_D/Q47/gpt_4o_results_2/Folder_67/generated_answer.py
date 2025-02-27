from string import ascii_letters

def palindromes_of_specific_lengths(s):
    result = set()
    s = s[65:100]
    s = ''.join((c for c in s if c in ascii_letters)).lower()
    length_range = range(26, 34)
    for start in range(len(s)):
        for length in length_range:
            end = start + length
            if end > len(s):
                break
            sub_s = s[start:end]
            if sub_s == sub_s[::-1]:
                result.add(sub_s)
    return result