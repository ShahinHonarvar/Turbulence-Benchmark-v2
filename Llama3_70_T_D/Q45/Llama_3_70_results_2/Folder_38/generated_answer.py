def palindromes_between_indices(s):
    s = s[3:9].lower()
    letters = [char for char in s if char.isalpha()]
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            substring = letters[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(''.join(substring))
    return palindromes