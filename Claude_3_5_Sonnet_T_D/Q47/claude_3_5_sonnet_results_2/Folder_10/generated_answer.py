def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[16:61]
    lowercase_substring = substring.lower()
    for length in range(16, 40):
        for i in range(len(substring) - length + 1):
            substr = lowercase_substring[i:i + length]
            if substr == substr[::-1] and substr.isalpha():
                result.add(substring[i:i + length])
    return result