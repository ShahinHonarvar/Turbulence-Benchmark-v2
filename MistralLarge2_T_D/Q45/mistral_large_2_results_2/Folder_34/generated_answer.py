def palindromes_between_indices(s):
    substring = s[5:8].lower()
    letters = [char for char in substring if char.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 3, len(letters) + 1):
            sub = letters[i:j]
            if sub == sub[::-1]:
                palindromes.add(''.join(sub))
    return palindromes