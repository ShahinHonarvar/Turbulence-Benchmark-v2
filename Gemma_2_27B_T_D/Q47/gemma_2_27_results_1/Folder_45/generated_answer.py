def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(70, 141):
        for j in range(i, min(i + 60, 141)):
            substring = text[i:j + 1].lower()
            if substring == substring[::-1] and len(substring) >= 3 and set(substring).issubset(set('abcdefghijklmnopqrstuvwxyz')):
                palindromes.add(substring)
    return palindromes