def palindromes_between_indices(s):
    letters = [ch for ch in s[4:7] if ch.isalpha()]
    letters = [ch.lower() for ch in letters]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 2, len(letters) + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(''.join(substring))
    return palindromes