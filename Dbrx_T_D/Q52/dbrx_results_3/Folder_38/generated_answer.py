def palindrome_of_length_n(text):
    n = 38
    palindromes = set()
    for i in range(len(text) - n + 1):
        substring = text[i:i + n].lower()
        if substring == ''.join(reversed(substring)) and substring.isalpha():
            palindromes.add(substring)
    return palindromes