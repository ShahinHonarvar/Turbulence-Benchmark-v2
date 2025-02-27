def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 55):
        substring = text[i:i + 56]
        if substring.lower() == substring.lower()[::-1]:
            palindromes.add(substring)
    return palindromes