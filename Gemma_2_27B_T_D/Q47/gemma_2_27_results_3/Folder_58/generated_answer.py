def palindromes_of_specific_lengths(text):
    sub_text = text[125:284]
    palindromes = set()
    for i in range(len(sub_text) - 108):
        for j in range(i + 109, min(i + 127, len(sub_text)) + 1):
            substring = sub_text[i:j].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes