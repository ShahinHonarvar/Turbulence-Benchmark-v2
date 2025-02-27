def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 317):
        substring = text[i:i + 318]
        if substring.lower() == substring.lower()[::-1]:
            palindromes.add(substring)
    return palindromes