def palindromes_between_indices(word):
    letters = ''.join([ch.lower() for ch in word[2:7] if ch.isalpha()])
    length = len(letters)
    if length < 4:
        return set()
    palindromes = set()
    for i in range(length):
        ch = letters[i]
        for j in range(i + 3, length):
            if len(set(letters[i:j + 1]) - set(ch)) == 0:
                palindromes.add(letters[i:j + 1])
    return palindromes