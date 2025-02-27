def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 24):
        j = i + 24
        if text[i:j + 1].lower() == text[i:j + 1][::-1].lower():
            palindromes.add(text[i:j + 1])
    return palindromes