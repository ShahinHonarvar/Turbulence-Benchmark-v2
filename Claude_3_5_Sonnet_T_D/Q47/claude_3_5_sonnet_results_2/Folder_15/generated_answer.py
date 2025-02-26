def palindromes_of_specific_lengths(s):
    result = set()
    s = s[:7].lower()
    for start in range(7):
        for end in range(start + 2, min(start + 6, 7)):
            substr = ''.join(filter(str.isalpha, s[start:end + 1]))
            if 3 <= len(substr) <= 6 and substr == substr[::-1]:
                result.add(substr)
    return result