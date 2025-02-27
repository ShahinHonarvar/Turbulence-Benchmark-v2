def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 94):
        substring = text[i:i + 95]
        if len(substring) == 95 and substring.lower() == substring.lower()[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes