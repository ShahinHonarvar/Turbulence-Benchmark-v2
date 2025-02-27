def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 39):
        substring = text[i:i + 40]
        if substring.lower() == substring.lower()[::-1]:
            palindromes.add(substring)
    return palindromes