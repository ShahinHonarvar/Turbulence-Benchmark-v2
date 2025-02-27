def palindrome_of_length_at_least_n(text):
    text = text.lower()
    palindromes = set()
    for length in range(24, len(text) + 1):
        for i in range(len(text) - length + 1):
            sub_text = text[i:i + length]
            if sub_text == sub_text[::-1]:
                palindromes.add(sub_text)
    return palindromes