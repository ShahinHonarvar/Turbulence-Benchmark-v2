def palindromes_between_indices(s):
    letters = s[8:10]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 2, len(letters) + 1):
            result = letters[i:j]
            if result == result[::-1]:
                palindromes.add(result.lower())
    return palindromes