def palindromes_between_indices(text):
    sub_text = text[0:6]
    letters = [char for char in sub_text if char.isalpha()]
    palindromes = set()
    for i in range(len(letters) - 3):
        for j in range(i + 4, len(letters) + 1):
            substring = ''.join(letters[i:j])
            if substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes