def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 2):
        substring = text[i:i + 3]
        if substring.lower() == substring.lower()[::-1] and substring.isalpha():
            palindromes.add(substring.lower())
    return palindromes