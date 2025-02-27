def palindromes_between_indices(text):
    letters = text[5:8]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                substring = letters[i:j] + letters[j:k] + letters[k:][::-1]
                if len(substring) >= 3 and substring.lower() == substring.lower()[::-1]:
                    palindromes.add(substring)
    return palindromes