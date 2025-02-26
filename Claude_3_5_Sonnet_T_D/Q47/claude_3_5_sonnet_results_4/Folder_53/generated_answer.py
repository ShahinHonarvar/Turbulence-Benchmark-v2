def palindromes_of_specific_lengths(s):
    result = set()
    s = s[1:300].lower()
    for i in range(len(s)):
        for length in range(3, 11):
            if i + length > len(s):
                break
            substring = s[i:i + length]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result