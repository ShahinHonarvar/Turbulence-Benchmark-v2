from re import findall

def palindromes_of_specific_lengths(input_string):
    palindrome_set = set()
    for length in range(154, 183):
        for index in range(101, 293 - length + 1):
            substring = input_string[index:index + length]
            palindrome = ''.join(findall('[a-zA-Z]', substring))
            if palindrome and palindrome == palindrome[::-1]:
                palindrome_set.add(palindrome)
    return palindrome_set