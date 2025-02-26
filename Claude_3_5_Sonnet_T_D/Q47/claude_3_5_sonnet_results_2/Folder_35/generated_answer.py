def palindromes_of_specific_lengths(s):
    substring = s[34:91]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 14, min(i + 40, len(substring) + 1)):
            substr = ''.join(filter(str.isalpha, substring[i:j])).lower()
            if 14 <= len(substr) <= 39 and substr == substr[::-1]:
                result.add(substr)
    return result