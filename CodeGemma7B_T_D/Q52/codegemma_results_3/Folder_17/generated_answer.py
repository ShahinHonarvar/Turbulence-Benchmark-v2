def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i:j + 1]
            if substring == substring[::-1]:
                if substring.lower() not in palindromes:
                    palindromes.add(substring.lower())
    if not palindromes:
        return {}
    return palindromes