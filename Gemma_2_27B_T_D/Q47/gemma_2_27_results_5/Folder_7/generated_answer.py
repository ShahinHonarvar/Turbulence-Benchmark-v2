def palindromes_of_specific_lengths(text):
    sub_text = text[119:257]
    palindromes = set()
    for i in range(len(sub_text) - 103):
        for j in range(i + 104, i + 124):
            substring = sub_text[i:j]
            if substring.lower() == substring[::-1].lower() and substring.isalpha():
                palindromes.add(substring)
    return palindromes