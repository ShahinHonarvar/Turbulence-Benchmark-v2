def palindromes_between_indices(string):
    s = string[3:10].lower()
    letters = []
    for i in range(len(s)):
        if ord(s[i]) >= 97 and ord(s[i]) <= 122:
            letters.append(s[i])
    result = set()
    for i in range(len(letters) + 1):
        for j in range(i, len(letters) + 1):
            substring = letters[i:j]
            if len(substring) >= 7:
                if substring == substring[::-1]:
                    result.add(''.join(substring))
    return result