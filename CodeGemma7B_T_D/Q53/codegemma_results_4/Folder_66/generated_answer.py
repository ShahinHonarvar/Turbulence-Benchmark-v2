def palindrome_of_length_at_least_n(text):
    lowercased_text = text.lower()
    palindromes = set()
    for i in range(len(lowercased_text)):
        for j in range(i + 76, len(lowercased_text) + 1):
            substring = lowercased_text[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes