def palindromes_between_indices(s):
    letters = [c.lower() for c in s[5:8]]
    result = set()
    for i in range(len(letters)):
        for j in range(i + 2, len(letters) + 1):
            if letters[i:j] == list(reversed(letters[i:j])):
                result.add(''.join(letters[i:j]))
    return result