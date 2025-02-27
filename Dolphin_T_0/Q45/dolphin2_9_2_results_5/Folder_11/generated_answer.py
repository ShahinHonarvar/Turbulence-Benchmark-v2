def palindromes_between_indices(s):
    letters = ''.join(sorted([char for char in s[3:8] if char.isalpha()]))
    palindromes = set()
    for i in range(len(letters) - 3):
        for j in range(i + 3, len(letters) + 1):
            if letters[i] == letters[j - 1] and letters[i + 1] == letters[j - 2] and (letters[i + 2] == letters[j - 3]):
                palindromes.add(letters[i:j])
    return palindromes