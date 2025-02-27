def palindromes_of_specific_lengths(text):
    found_palindromes = set()
    text = text.lower()
    for i in range(39, 95):
        for j in range(i, 95):
            substring = text[i:j + 1]
            if substring == substring[::-1] and len(substring) >= 14 and (len(substring) <= 52):
                found_palindromes.add(substring)
    return found_palindromes or set()