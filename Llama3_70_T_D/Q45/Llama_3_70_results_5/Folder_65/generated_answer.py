def palindromes_between_indices(s):
    s = s[:7].lower()
    letters = [c for c in s if c.isalpha()]
    if len(letters) < 5:
        return set()
    result = set()
    for i in range(len(letters)):
        for j in range(i + 5, len(letters) + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                result.add(''.join(substring))
    return result