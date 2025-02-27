def palindromes_of_specific_lengths(s):
    s = s[15:78].lower()
    lengths = [43, 44, 45, 46, 47]
    result = set()
    for length in lengths:
        s_length = len(s)
        for i in range(s_length - length + 1):
            sub_s = s[i:i + length]
            if sub_s == sub_s[::-1]:
                result.add(sub_s)
    return result