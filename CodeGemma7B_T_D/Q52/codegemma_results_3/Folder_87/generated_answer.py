def palindrome_of_length_n(text):
    palindrome = set()
    for i in range(len(text) - 56):
        for j in range(i + 1, len(text) - 56 + 1):
            palindromic_text = text[i:j]
            if palindromic_text == palindromic_text[::-1].lower():
                palindrome.add(palindromic_text)
    return palindrome