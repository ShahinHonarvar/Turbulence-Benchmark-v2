def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 445 + 1):
        substring = text[i:i + 445]
        if substring.lower() == substring.lower()[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes