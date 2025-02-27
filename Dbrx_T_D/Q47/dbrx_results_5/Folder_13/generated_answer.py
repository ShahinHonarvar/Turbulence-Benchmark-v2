def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(13, 96):
        for length in range(57, 61):
            if i + length <= len(s):
                substring = s[i:i + length].lower()
                if substring == substring[::-1] and substring.isalpha():
                    result.add(substring)
    return result