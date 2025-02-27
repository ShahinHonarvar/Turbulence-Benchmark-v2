def palindromes_between_indices(string):
    palindromes = set()
    for i in range(3, 9):
        for j in range(i + 2, len(string) + 1):
            substring = string[i:j]
            if len(substring) >= 5:
                substring = ''.join((ch.lower() for ch in substring if ch.isalpha()))
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes