def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[1:4])).lower()
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            substring = letters[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes