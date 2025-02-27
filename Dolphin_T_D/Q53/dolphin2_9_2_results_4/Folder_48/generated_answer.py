def palindrome_of_length_at_least_n(text):
    text = text.lower()
    palindromes = set()
    for i in range(len(text) - 150):
        for j in range(i + 150, len(text) + 1):
            sub_text = text[i:j]
            if sub_text == sub_text[::-1] and sub_text.isalpha():
                palindromes.add(sub_text)
    return palindromes