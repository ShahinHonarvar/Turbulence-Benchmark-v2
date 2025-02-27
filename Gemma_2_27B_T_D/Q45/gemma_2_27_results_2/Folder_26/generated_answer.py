def palindromes_between_indices(text):
    substring = text[4:7]
    letters = [char for char in substring if char.isalpha()]
    palindromes = set()
    for i in range(len(letters) - 2):
        for j in range(i + 3, len(letters) + 1):
            candidate = ''.join(letters[i:j]).lower()
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes