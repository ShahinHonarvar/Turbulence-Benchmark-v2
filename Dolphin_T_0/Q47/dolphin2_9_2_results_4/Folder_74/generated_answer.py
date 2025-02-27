def palindromes_of_specific_lengths(string):
    relevant_sub_string = string[30:85]
    necessary_lengths = range(12, 21)
    palindrome_set = set()
    for length in necessary_lengths:
        for i in range(len(relevant_sub_string) - length + 1):
            sub_string = relevant_sub_string[i:i + length]
            if sub_string == sub_string[::-1] and sub_string.isalpha():
                palindrome_set.add(sub_string.lower())
    return palindrome_set