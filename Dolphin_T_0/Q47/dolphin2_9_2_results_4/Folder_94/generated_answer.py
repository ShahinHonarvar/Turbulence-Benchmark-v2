def palindromes_of_specific_lengths(input_string):
    input_length = len(input_string)
    subset_string = input_string[40:95]
    palindrome_set = set()
    if input_length < 95:
        return palindrome_set
    for palindrome_length in range(45, 52):
        for index in range(0, input_length - palindrome_length + 1):
            sub_string = subset_string[index:index + palindrome_length]
            if sub_string == sub_string[::-1] and sub_string.isalpha():
                palindrome_set.add(sub_string.lower())
    return palindrome_set