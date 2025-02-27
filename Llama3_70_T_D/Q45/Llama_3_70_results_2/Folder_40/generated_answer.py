def palindromes_between_indices(s):
    s = s[4:10].lower()
    letters = [c for c in s if c.isalpha()]
    if len(letters) < 7:
        return set()
    result = set()
    for i in range(len(letters)):
        for j in range(i + 7, len(letters) + 1):
            substr = letters[i:j]
            for k in range(len(substr) // 2):
                if substr[k] != substr[-k - 1]:
                    break
            else:
                result.add(''.join(substr))
    return result