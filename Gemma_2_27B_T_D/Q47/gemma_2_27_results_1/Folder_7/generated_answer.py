def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(119, 257):
        for j in range(i, min(i + 123, 257)):
            substring = text[i:j].lower()
            if substring == substring[::-1] and 104 <= len(substring) <= 123 and substring.isalpha():
                palindromes.add(substring)
    return palindromes