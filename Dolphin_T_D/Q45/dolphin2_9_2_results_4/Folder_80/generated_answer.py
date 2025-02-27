def palindromes_between_indices(s):
    letters = [ch for ch in s[3:9] if ch.isalpha() and ch.isascii()]
    if len(letters) < 7:
        return set()
    letters = [ch.lower() for ch in letters]
    palindromes = set()
    for p in range(7, len(letters) + 1):
        for i in range(len(letters) - p + 1):
            if letters[i:i + p] == list(reversed(letters[i:i + p])):
                palindromes.add(''.join(letters[i:i + p]))
    return palindromes