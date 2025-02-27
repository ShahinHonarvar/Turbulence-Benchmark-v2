def palindromes_between_indices(text):
    letters = sorted(text[1:4].lower())
    palindromes = set()
    for i in range(len(letters) - 3):
        for j in range(i + 4, len(letters) + 1):
            candidate = ''.join(letters[i:j])
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes