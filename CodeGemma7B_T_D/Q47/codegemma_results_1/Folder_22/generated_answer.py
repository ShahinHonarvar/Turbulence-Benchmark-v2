def palindromes_of_specific_lengths(text):
    target_substring = text[100:201]
    palindromes = set()
    for i in range(len(target_substring)):
        for j in range(i + 5, i + 11):
            substring = target_substring[i:j].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes