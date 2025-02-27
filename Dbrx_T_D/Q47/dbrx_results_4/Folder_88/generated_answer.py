def palindromes_of_specific_lengths(input_string):
    palindrome_set = set()
    for i in range(11, 88):
        for j in range(4, 6):
            if i + j <= 100:
                substring = input_string[i:i + j].lower()
                if substring == substring[::-1] and substring.isalpha():
                    palindrome_set.add(substring)
    return palindrome_set