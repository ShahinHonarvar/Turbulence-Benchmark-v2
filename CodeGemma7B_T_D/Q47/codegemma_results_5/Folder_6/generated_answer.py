def palindromes_of_specific_lengths(text):
    palindrome_set = set()
    for i in range(45, 99):
        for j in range(40, 48):
            if len(text) >= i + j:
                substring = text[i:i + j].lower()
                if substring == substring[::-1] and substring.isalpha():
                    palindrome_set.add(substring)
    return palindrome_set