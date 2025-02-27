def palindromes_between_indices(s):
    letters = s[6:10]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 3, len(letters) + 1):
            if letters[i:j] == letters[i:j][::-1]:
                palindromes.add(letters[i:j])
    return palindromes