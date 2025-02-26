def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[23:95]
    substring = ''.join(filter(str.isalpha, substring)).lower()
    for i in range(len(substring)):
        for j in range(i + 17, min(i + 56, len(substring) + 1)):
            substr = substring[i:j]
            if substr == substr[::-1] and 17 <= len(substr) <= 55:
                result.add(substr)
    return result