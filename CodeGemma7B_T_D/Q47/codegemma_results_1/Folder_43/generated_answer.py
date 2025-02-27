def palindromes_of_specific_lengths(text):
    text = text.lower()
    target_substring = text[40:90]
    palindromes = set()
    for i in range(len(target_substring) - 22):
        for j in range(23, len(target_substring) - i):
            substring = target_substring[i:i + j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes