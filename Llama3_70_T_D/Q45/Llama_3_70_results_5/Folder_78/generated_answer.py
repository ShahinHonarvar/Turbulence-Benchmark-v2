def palindromes_between_indices(s):
    letters = set((s[i].lower() for i in range(6, 9) if s[i].isalpha()))
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for p in __import__('itertools').product(letters, repeat=length):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes