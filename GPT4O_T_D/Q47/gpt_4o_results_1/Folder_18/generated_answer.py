def palindromes_of_specific_lengths(s):
    s = s[11:84]
    s = ''.join(filter(str.isalpha, s))
    result = set()
    for i in range(len(s)):
        for j in range(i + 13, min(i + 67, len(s) + 1)):
            substring = s[i:j]
            if substring.lower() == substring[::-1].lower():
                result.add(substring)
    return result