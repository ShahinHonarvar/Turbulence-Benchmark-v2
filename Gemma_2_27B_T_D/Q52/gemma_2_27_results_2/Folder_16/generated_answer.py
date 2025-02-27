def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 254):
        substring = text[i:i + 255].lower()
        if substring == substring[::-1]:
            if substring.isalpha():
                palindromes.add(substring)
    return palindromes