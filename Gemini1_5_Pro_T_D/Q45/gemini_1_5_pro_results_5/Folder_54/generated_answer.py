def palindromes_between_indices(string):
    letters = set([char.lower() for char in string[4:10] if char.isalpha()])
    palindromes = set()
    for i in range(4, len(string) + 1):
        for j in range(0, len(string) - i + 1):
            substring = string[j:j + i]
            if len(substring) >= 4 and substring.lower() == substring[::-1].lower() and set([char.lower() for char in substring if char.isalpha()]).issubset(letters):
                palindromes.add(substring)
    return palindromes