def palindromes_of_specific_lengths(s):
    s = s[62:89].lower()
    result = set()
    for length in range(18, 22):
        for i in range(len(s) - length + 1):
            sub_s = s[i:i + length]
            if sub_s == sub_s[::-1] and sub_s.isalpha():
                result.add(sub_s)
    return result