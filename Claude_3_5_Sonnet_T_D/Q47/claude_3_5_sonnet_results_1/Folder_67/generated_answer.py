def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[65:100]
    lowercase_substring = substring.lower()
    for length in range(26, 34):
        for i in range(len(substring) - length + 1):
            substr = lowercase_substring[i:i + length]
            if substr.isalpha() and substr == substr[::-1]:
                result.add(substring[i:i + length])
    return result