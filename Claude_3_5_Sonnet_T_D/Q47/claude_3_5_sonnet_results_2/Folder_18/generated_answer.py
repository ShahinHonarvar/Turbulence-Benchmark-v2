def palindromes_of_specific_lengths(s):
    substring = s[11:84]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 13, min(i + 67, len(substring) + 1)):
            if j - i > 66:
                break
            substr = ''.join((char for char in substring[i:j] if char.isalpha()))
            if substr.lower() == substr.lower()[::-1] and 13 <= len(substr) <= 66:
                result.add(substr)
    return result