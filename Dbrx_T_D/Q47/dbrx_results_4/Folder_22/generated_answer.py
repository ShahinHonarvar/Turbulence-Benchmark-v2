def palindromes_of_specific_lengths(string):
    palindrome_set = set()
    for index in range(100, 201):
        for length in range(5, 11):
            if index + length - 1 < 200:
                substring = string[index:index + length].lower()
                if substring == substring[::-1] and substring.isalpha():
                    palindrome_set.add(substring)
    return palindrome_set