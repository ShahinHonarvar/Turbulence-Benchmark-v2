def palindromes_of_specific_lengths(text):
    result = set()
    for i in range(12, 57):
        for j in range(i + 20, i + 22):
            if j <= 56:
                substring = text[i:j].lower()
                if substring == substring[::-1] and substring.isalpha():
                    result.add(text[i:j])
    return result