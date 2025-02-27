def palindromes_of_specific_lengths(string):
    split_string = [char.lower() for char in string]
    palindromes = set()
    for index in range(0, 6):
        for j in range(index + 2, 7):
            substring = split_string[index:j]
            if substring == substring[::-1]:
                palindrome = ''.join(substring)
                if palindrome.isalpha():
                    palindromes.add(palindrome)
    return palindromes or {}