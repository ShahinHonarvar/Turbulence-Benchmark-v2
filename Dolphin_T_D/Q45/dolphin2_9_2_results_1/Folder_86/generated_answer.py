def palindromes_between_indices(input_string):
    substring = input_string[6:10]
    palindrome_set = set()
    for i in range(len(substring)):
        for j in range(i + 3, len(substring) + 1):
            subword = substring[i:j]
            if subword == subword[::-1]:
                palindrome_set.add(subword.lower())
    return palindrome_set