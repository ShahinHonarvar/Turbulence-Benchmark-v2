def palindromes_between_indices(string):
    s = string[4:9].lower()
    letters = []
    for c in s:
        if ord('a') <= ord(c) <= ord('z'):
            letters.append(c)
    result = set()
    if len(letters) >= 4:
        for i in range(len(letters) - 3):
            for j in range(i + 3, len(letters) + 1):
                substring = letters[i:j]
                if substring == substring[::-1]:
                    result.add(''.join(substring))
    return result