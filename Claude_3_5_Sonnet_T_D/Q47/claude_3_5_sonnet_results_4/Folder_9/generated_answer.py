def palindromes_of_specific_lengths(s):
    result = set()
    s = s[:301].lower()
    for i in range(len(s)):
        for j in range(i + 50, min(i + 61, len(s) + 1)):
            substring = ''.join(filter(str.isalpha, s[i:j]))
            if len(substring) >= 50 and substring == substring[::-1]:
                result.add(substring)
    return result