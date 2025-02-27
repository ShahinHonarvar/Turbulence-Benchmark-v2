def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 58):
        substring = text[i:i + 59]
        if len(substring) == 59 and substring.lower() == substring.lower()[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes