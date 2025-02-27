def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 71):
        substring = text[i:i + 72]
        if substring.lower() == substring.lower()[::-1]:
            palindromes.add(substring)
    return palindromes