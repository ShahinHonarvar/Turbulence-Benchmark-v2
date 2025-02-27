def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 444):
        substring = s[i:i + 445]
        if substring.lower() == substring.lower()[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes