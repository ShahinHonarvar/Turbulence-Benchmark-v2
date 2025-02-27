def palindromes_of_specific_lengths(s):
    s = s[39:95]
    result = set()
    for length in range(14, 53):
        for i in range(len(s) - length + 1):
            s_substring = s[i:i + length]
            if s_substring == s_substring[::-1] and s_substring.isalpha():
                result.add(s_substring.lower())
    return result