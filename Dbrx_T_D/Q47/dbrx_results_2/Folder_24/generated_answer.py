def palindromes_of_specific_lengths(input_string):
    palindrome_set = set()
    for i in range(12, 93):
        for j in range(42, 78):
            if i + j > 100:
                break
            substring = input_string[i:i + j].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindrome_set.add(substring)
    return palindrome_set