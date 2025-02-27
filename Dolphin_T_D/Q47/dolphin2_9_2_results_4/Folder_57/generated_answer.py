def palindromes_of_specific_lengths(string):
    sub_string = string[16:95]
    palindrome_set = set()
    for length in range(39, 53):
        for index in range(len(sub_string) - length + 1):
            sub_str = sub_string[index:index + length]
            if sub_str == sub_str[::-1].lower():
                palindrome_set.add(sub_str)
    return palindrome_set