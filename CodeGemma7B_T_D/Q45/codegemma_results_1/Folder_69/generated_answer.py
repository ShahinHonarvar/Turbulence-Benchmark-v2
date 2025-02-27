def palindromes_between_indices(text):
    text = text.lower()
    palindromes = set()
    letters = [ch for ch in text if ch.isalpha()]
    for i in range(len(letters) - 3):
        substring = ''.join(letters[i:i + 4])
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes