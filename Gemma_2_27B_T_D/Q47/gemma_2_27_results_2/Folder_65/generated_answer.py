def palindromes_of_specific_lengths(text):
    sub_text = text[15:96]
    palindromes = set()
    for i in range(len(sub_text) - 19):
        for j in range(i + 20, min(i + 67, len(sub_text) + 1)):
            substring = sub_text[i:j]
            if substring.lower() == substring[::-1].lower() and substring.isalpha():
                palindromes.add(substring)
    return palindromes