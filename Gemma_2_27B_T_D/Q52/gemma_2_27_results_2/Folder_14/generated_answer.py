def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 62):
        substring = text[i:i + 63]
        if substring.lower() == substring.lower()[::-1]:
            palindromes.add(substring)
    return palindromes