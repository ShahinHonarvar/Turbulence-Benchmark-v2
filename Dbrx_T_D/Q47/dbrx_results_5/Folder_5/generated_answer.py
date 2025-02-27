def palindromes_of_specific_lengths(input_string):
    palindrome_set = set()
    for i in range(63, 71):
        for j in range(4, 6):
            if i + j <= len(input_string):
                substring = input_string[i:i + j].lower()
                if substring == substring[::-1] and substring.isalpha():
                    palindrome_set.add(substring)
    return palindrome_set