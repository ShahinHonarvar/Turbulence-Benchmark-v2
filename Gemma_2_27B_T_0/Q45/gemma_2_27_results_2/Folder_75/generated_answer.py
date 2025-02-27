def palindromes_between_indices(text):
    letters = text[2:5]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                substring = letters[i:j + 1] + letters[j:i:-1]
                if len(substring) >= 3 and substring.lower() == substring[::-1].lower():
                    palindromes.add(substring)
    return palindromes