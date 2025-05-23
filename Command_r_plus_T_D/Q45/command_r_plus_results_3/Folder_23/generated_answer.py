def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    letters = ''.join(filter(str.isalpha, s[:7])).lower()
    for i in range(len(letters)):
        for j in range(i + 4, len(letters) + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes