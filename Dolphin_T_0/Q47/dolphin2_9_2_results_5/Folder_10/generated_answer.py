def palindromes_of_specific_lengths(s):
    s = s[16:61]
    result = set()
    for length in range(16, 40):
        for i in range(len(s) - length + 1):
            sub_s = s[i:i + length]
            if all(('a' <= char.lower() <= 'z' for char in sub_s)) and sub_s == sub_s[::-1]:
                result.add(sub_s)
    return result