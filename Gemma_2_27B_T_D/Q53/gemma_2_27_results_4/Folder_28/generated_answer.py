def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 41):
        substring = text[i:i + 42]
        if substring.lower() == substring[::-1].lower():
            palindromes.add(substring)
    return palindromes