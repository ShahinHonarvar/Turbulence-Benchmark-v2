def palindromes_of_specific_lengths(the_string):

    def is_palindrome(sub_string):
        return sub_string == sub_string[::-1]
    the_substring = the_string[18:88]
    palindromes_set = set()
    for length in range(38, 61):
        for start_index in range(len(the_substring) - length + 1):
            a_substring = the_substring[start_index:start_index + length]
            if a_substring.isalpha() and is_palindrome(a_substring.lower()):
                palindromes_set.add(a_substring)
    return palindromes_set