def palindromes_of_specific_lengths(s):
    s = s[11:92]
    result = set()
    for i in range(17, 67):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                result.add(substring)
    return result