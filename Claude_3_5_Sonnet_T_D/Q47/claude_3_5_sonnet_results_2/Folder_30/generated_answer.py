def palindromes_of_specific_lengths(s):
    substring = s[14:91].lower()
    result = set()
    for i in range(len(substring)):
        for j in range(i + 55, min(i + 72, len(substring) + 1)):
            substr = substring[i:j]
            if substr == substr[::-1] and substr.isalpha():
                result.add(substr)
    return result