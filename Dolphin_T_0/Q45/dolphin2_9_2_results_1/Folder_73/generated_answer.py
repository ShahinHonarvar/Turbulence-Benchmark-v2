def palindromes_between_indices(s):
    letters = ''
    for i in range(3, 7):
        if s[i].isalpha():
            letters += s[i].lower()
    palindromes = set()
    length = len(letters)
    for i in range(3, length + 1):
        for j in range(len(letters) - i + 1):
            word = letters[j:j + i]
            if word == word[::-1]:
                palindromes.add(word)
                if len(word) > 2:
                    palindromes.add(word[::-1])
    return palindromes