def palindromes_of_specific_lengths(input_string):
    palindrome_set = set()
    for i in range(127, 289):
        for j in range(i - 118, i + 142):
            substring = input_string[i:j]
            if len(substring) >= 119 and len(substring) <= 141:
                if substring == substring[::-1] and substring.isalpha():
                    palindrome_set.add(substring.lower())
    return palindrome_set