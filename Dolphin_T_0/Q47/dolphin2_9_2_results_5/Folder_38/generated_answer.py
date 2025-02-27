def palindromes_of_specific_lengths(s):
    s = s[18:88]
    result = set()
    for length in range(38, 61):
        for begin in range(0, len(s)):
            if s[begin:begin + length] == s[begin:begin + length][::-1] and s[begin:begin + length].isalpha():
                result.add(s[begin:begin + length].lower())
    return result