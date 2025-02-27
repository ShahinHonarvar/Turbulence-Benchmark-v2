def palindromes_between_indices(s):
    s = s[3:10].lower()
    letters = [char for char in s if char.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 5, len(letters) + 1):
            substring = ''.join(letters[i:j])
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes