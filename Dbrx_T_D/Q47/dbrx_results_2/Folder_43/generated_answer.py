def palindromes_of_specific_lengths(input_string):
    palindrome_set = set()
    for i in range(41, 90):
        for j in range(23, 39):
            if i + j - 1 <= len(input_string):
                substring = input_string[i - 1:i + j - 1].lower()
                if substring == substring[::-1]:
                    palindrome_set.add(substring)
    return palindrome_set