def palindromes_between_indices(s):
    chars = [c.lower() for c in s[5:9]]
    letters = ''.join([c for c in chars if c.isalpha()])
    if len(letters) < 3:
        return set()
    palindromes = set()
    length = len(letters)
    for i in range(length):
        for j in range(i + 2, length + 1):
            subs = letters[i:j]
            if subs == subs[::-1]:
                palindromes.add(subs)
    return palindromes